"""Carruseles con estilo "holo" (degradados animados en los colores del feed: magenta, naranja,
lima y violeta). Cada slide sale en PNG (1080x1350) y en MP4 de 6 s en loop.

Uso:  python3 contenido/carruseles/generar_holo.py && node contenido/carruseles/render_holo.js
"""
import html, json, pathlib

BASE = pathlib.Path(__file__).parent
OUT_HTML = BASE / "_html"
OUT_HTML.mkdir(exist_ok=True)

# base = color de fondo; blobs = manchas de color que se mueven; ink = texto
PALETAS = {
    "magenta": {"base": "#FF4FA8", "blobs": ["#FF8A3D", "#B54CFF", "#FF2E8A", "#FFB15C"], "ink": "#17061A", "card": "rgba(255,255,255,.55)", "chip_bg": "#17061A", "chip_fg": "#FFFFFF"},
    "lima":    {"base": "#C6F432", "blobs": ["#E9FF6B", "#7EE84A", "#FF7AD0", "#F4FF9E"], "ink": "#0E1405", "card": "rgba(255,255,255,.5)", "chip_bg": "#0E1405", "chip_fg": "#C6F432"},
    "violeta": {"base": "#A27BFF", "blobs": ["#FF6CC6", "#5C86FF", "#F0B8FF", "#C6F432"], "ink": "#140A2E", "card": "rgba(255,255,255,.5)", "chip_bg": "#140A2E", "chip_fg": "#FFFFFF"},
    "naranja": {"base": "#FF8A4C", "blobs": ["#FF4FA0", "#FFC94D", "#FF5E3A", "#FFB3D9"], "ink": "#1E0A04", "card": "rgba(255,255,255,.5)", "chip_bg": "#1E0A04", "chip_fg": "#FFFFFF"},
    "noche":   {"base": "#0E0B12", "blobs": ["#FF4FA8", "#6A2CE8", "#2A1260", "#FF7A3D"], "ink": "#FFFFFF", "card": "rgba(255,255,255,.1)", "chip_bg": "#C6F432", "chip_fg": "#0E0B12", "bo": ".55"},
}

CSS = """
@import url('../_fuentes/local.css');
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--base);color:var(--ink);font-family:'Instrument Sans',sans-serif;overflow:hidden;position:relative}
.bg{position:absolute;inset:-200px;filter:blur(90px) saturate(1.15)}
.blob{position:absolute;border-radius:50%;width:var(--s);height:var(--s);background:var(--c);opacity:var(--bo,.9);will-change:transform}
.grain{position:absolute;inset:0;opacity:.09;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.top{position:absolute;z-index:3;top:56px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;
     font-weight:700;font-size:24px;letter-spacing:.16em;text-transform:uppercase}
.top .n{opacity:.65}
.foot{position:absolute;z-index:3;bottom:54px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:700}
.arrow{display:inline-block}
.wrap{z-index:2;position:absolute;left:84px;right:84px;top:160px;bottom:140px;display:flex;flex-direction:column;justify-content:center}
h1{font-weight:700;letter-spacing:-.035em;line-height:.93}
.chip{display:inline-block;background:var(--chip_bg);color:var(--chip_fg);font-weight:700;font-size:28px;
      padding:12px 26px;border-radius:100px;letter-spacing:.08em;text-transform:uppercase;align-self:flex-start}
p{font-size:40px;line-height:1.3;font-weight:500}
p b, li b{font-weight:700}
.num{font-weight:700;letter-spacing:-.06em;font-size:230px;line-height:.8}
.card{background:var(--card);backdrop-filter:blur(6px);border-radius:34px;padding:34px 40px}
.tip{margin-top:34px;display:flex;gap:18px;align-items:flex-start;font-size:34px;line-height:1.3;font-weight:600}
.tip .k{flex:none;font-size:24px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;background:var(--chip_bg);color:var(--chip_fg);border-radius:100px;padding:8px 18px;margin-top:4px}
.lista{list-style:none;margin-top:38px;display:flex;flex-direction:column;gap:20px}
.lista li{font-size:40px;line-height:1.25;padding:22px 30px;border-radius:26px;background:var(--card)}
.aviso{font-size:22px;opacity:.85;margin-top:26px;font-weight:500}
"""

JS = """
<script>
// t va de 0 a 1 y vuelve al inicio: el video hace loop sin salto.
const B=[...document.querySelectorAll('.blob')];
function setT(t){
  const a=t*Math.PI*2;
  B.forEach((b,i)=>{
    const k=i+1, r=120+40*i;
    const x=Math.cos(a*(i%2?1:-1)+k*1.7)*r, y=Math.sin(a*(i%3?1:-1)+k*2.3)*r*0.9;
    const s=1+0.12*Math.sin(a+k);
    b.style.transform=`translate(${x}px,${y}px) scale(${s})`;
  });
  const ar=document.querySelector('.arrow'); if(ar) ar.style.transform=`translateX(${Math.max(0,Math.sin(a*2))*14}px)`;
}
setT(0);
</script>"""


def e(t):  # escapa y permite **negrita**
    t = html.escape(t)
    partes = t.split("**")
    return "".join(f"<b>{x}</b>" if i % 2 else x for i, x in enumerate(partes)).replace("\n", "<br>")


def fondo(p):
    pos = [(-80, -60, 900), (520, 160, 820), (60, 760, 880), (560, 980, 760)]
    blobs = "".join(f'<div class="blob" style="left:{x}px;top:{y}px;--s:{s}px;--c:{c}"></div>' for (x, y, s), c in zip(pos, p["blobs"]))
    return f'<div class="bg">{blobs}</div><div class="grain"></div>'


def pagina(paleta, i, total, cuerpo, pie):
    p = PALETAS[paleta]
    vars_ = ";".join(f"--{k}:{v}" for k, v in p.items() if k != "blobs")
    derecha = '<span>Desliza <span class="arrow">→</span></span>' if i < total else f"<span>{e(pie)}</span>"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body style="{vars_}">{fondo(p)}
<div class="top"><span>FPROJECT · BAREFOOT</span><span class="n">{i:02d}/{total:02d}</span></div>
<div class="wrap">{cuerpo}</div>
<div class="foot"><span>@fproject_at</span>{derecha}</div>{JS}
</body></html>"""


CARRUSELES = {
"05-elegir-calzado": {
    "pie": "Comenta PREVENTA",
    "slides": [
        ("magenta", "portada", dict(chip="Guía de fisio", titulo="Antes de\ncomprar\nzapatos, haz\nestas 5 pruebas", sub="Te toman **1 minuto** en la tienda.")),
        ("lima", "prueba", dict(n="1", titulo="Dóblalo", texto="Lleva la punta hacia arriba. Debe doblarse **donde se doblan tus dedos**, no en la mitad.", ok="Se dobla fácil, como tu pie.")),
        ("violeta", "prueba", dict(n="2", titulo="Retuércelo", texto="Gíralo como si escurrieras un trapo. Si **no cede nada**, tu pie tampoco podrá adaptarse al suelo.", ok="Cede y vuelve a su forma.")),
        ("naranja", "prueba", dict(n="3", titulo="La plantilla", texto="Sácala y párate encima descalzo. Si **tus dedos se salen por los lados**, el zapato es más estrecho que tu pie.", ok="Todo tu pie cabe dentro.")),
        ("magenta", "prueba", dict(n="4", titulo="Míralo de lado", texto="¿El talón está más alto que la punta? Eso es un **mini tacón** (drop). Cambia cómo apoyas todo el cuerpo.", ok="Talón y punta al mismo nivel.")),
        ("lima", "prueba", dict(n="5", titulo="Mueve los dedos", texto="Con el zapato puesto, ábrelos y muévelos. Deja **un dedo de espacio** entre tu dedo más largo y la punta.", ok="Tus dedos se abren sin chocar.")),
        ("violeta", "texto", dict(titulo="Bonus:\ncompra en\nla tarde", texto="Tus pies se **hinchan un poco** a lo largo del día. Si te quedan bien a las 6 p. m., te quedan bien siempre.")),
        ("noche", "cta", dict(titulo="Guárdalo para\ntu próxima\ncompra", texto="KIBA pasa las 5 pruebas. La preventa abre **a finales de octubre**.\n\n💬 Comenta **PREVENTA** y entra a la lista VIP.", accion="Comenta PREVENTA", firma="Fredd Medina · Fisioterapeuta")),
    ],
},
"06-lo-que-viene-kiba": {
    "pie": "Comenta PREVENTA",
    "slides": [
        ("noche", "portada", dict(chip="Lo que viene", titulo="KIBA\nya casi\nllega", sub="El barefoot que diseñamos\n**desde la fisioterapia**.", tam=200)),
        ("naranja", "texto", dict(titulo="Cambio de\nplanes", texto="Te dijimos 15 de octubre. Movimos la preventa a **finales de octubre** para que esperes menos tu par después de pagar.\n\nPreferimos decírtelo claro.")),
        ("lima", "lista", dict(titulo="Qué es KIBA", items=["**Puntera ancha:** tus dedos se abren", "**Cero drop:** talón y punta al mismo nivel", "**Suela flexible:** tu pie siente el suelo", "**Plantilla de transición** incluida"])),
        ("violeta", "lista", dict(titulo="Para quién", items=["Para **entrenar**: sentadilla, peso muerto, saltos", "Para el **día a día**", "Para quien quiere pasarse al barefoot **con guía de un fisio**"])),
        ("magenta", "texto", dict(titulo="Tallas 36–45\n3 colores", texto="**Verde, Amarillo y Negro.**\n\nAntes de la preventa te compartimos la guía de tallas para que aciertes a la primera.")),
        ("lima", "lista", dict(titulo="Lista VIP", items=["Te mando el **link antes que al público**", "🎁 **Separadores F Movement de regalo** si compras en la preventa", "Plan de transición de **8 semanas**"])),
        ("noche", "cta", dict(titulo="¿Quieres\nentrar?", texto="💬 Comenta **PREVENTA** y te escribo por DM.\n\nTe pido tu talla y tu color para tenerte todo listo.", accion="Comenta PREVENTA", firma="Preventa · finales de octubre")),
    ],
},
}


def slide(tipo, d):
    if tipo == "portada":
        return f"""<span class="chip">{e(d['chip'])}</span>
<h1 style="font-size:{d.get('tam',140)}px;margin-top:40px">{e(d['titulo'])}</h1>
<p style="margin-top:44px">{e(d['sub'])}</p>"""
    if tipo == "prueba":
        return f"""<div class="num">{e(d['n'])}</div><h1 style="font-size:120px;margin-top:6px">{e(d['titulo'])}</h1>
<p style="margin-top:34px">{e(d['texto'])}</p>
<div class="card tip"><span class="k">Bien</span><span>{e(d['ok'])}</span></div>"""
    if tipo == "texto":
        return f"""<h1 style="font-size:130px">{e(d['titulo'])}</h1><p style="margin-top:48px">{e(d['texto'])}</p>"""
    if tipo == "lista":
        items = "".join(f"<li>{e(x)}</li>" for x in d["items"])
        return f"""<h1 style="font-size:130px">{e(d['titulo'])}</h1><ul class="lista">{items}</ul>"""
    if tipo == "cta":
        return f"""<h1 style="font-size:120px">{e(d['titulo'])}</h1><p style="margin-top:36px">{e(d['texto'])}</p>
<div style="margin-top:54px"><span class="chip" style="font-size:38px;padding:22px 40px">{e(d['accion'])}</span></div>
<p style="margin-top:44px;font-size:28px;font-weight:700;letter-spacing:.1em;text-transform:uppercase">{e(d['firma'])}</p>
<p class="aviso">Contenido educativo. No reemplaza una valoración profesional.</p>"""
    raise ValueError(tipo)


lista = []
for nombre, c in CARRUSELES.items():
    slides = c["slides"]
    (BASE / nombre).mkdir(exist_ok=True)
    for i, (pal, tipo, d) in enumerate(slides, 1):
        f = OUT_HTML / f"{nombre}-{i:02d}.html"
        f.write_text(pagina(pal, i, len(slides), slide(tipo, d), c["pie"]), encoding="utf-8")
        lista.append({"html": str(f), "png": str(BASE / nombre / f"{i:02d}.png"), "mp4": str(BASE / nombre / f"{i:02d}.mp4")})
(OUT_HTML / "lista_holo.json").write_text(json.dumps(lista, indent=1))
print(len(lista), "slides")
