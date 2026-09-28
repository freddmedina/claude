"""Genera los HTML de los carruseles de prelanzamiento (1080x1350) y luego
render.js los convierte a PNG con Chromium.

Uso:  python3 contenido/carruseles/generar.py && node contenido/carruseles/render.js
"""
import html, json, pathlib

BASE = pathlib.Path(__file__).parent
OUT_HTML = BASE / "_html"
OUT_HTML.mkdir(exist_ok=True)

TEMAS = {
    "lima":   {"bg": "#B8F03C", "fg": "#0B0B0B", "acento": "#0B0B0B", "sub": "#1d2a05", "chip_bg": "#0B0B0B", "chip_fg": "#B8F03C"},
    "negro":  {"bg": "#0B0B0B", "fg": "#F6F3EC", "acento": "#B8F03C", "sub": "#cfcac0", "chip_bg": "#B8F03C", "chip_fg": "#0B0B0B"},
    "rosa":   {"bg": "linear-gradient(170deg,#F45BC6 0%,#F77A9A 50%,#FF9A4A 100%)", "fg": "#0B0B0B", "acento": "#FFFFFF", "sub": "#2a0f22", "chip_bg": "#0B0B0B", "chip_fg": "#FFFFFF"},
    "crema":  {"bg": "#F1EDE7", "fg": "#0B0B0B", "acento": "#0B0B0B", "sub": "#3b3833", "chip_bg": "#B8F03C", "chip_fg": "#0B0B0B"},
}

CSS = """
@import url('../_fuentes/local.css');
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--fg);font-family:'Instrument Sans',sans-serif;overflow:hidden;position:relative}
.top{position:absolute;top:56px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:center;
     font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase}
.top .n{opacity:.7}
.foot{position:absolute;bottom:56px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:center;
      font-size:26px;font-weight:600}
.wrap{z-index:2;position:absolute;left:90px;right:90px;top:170px;bottom:150px;display:flex;flex-direction:column;justify-content:center}
h1{font-family:'Bebas Neue',sans-serif;font-weight:400;text-transform:uppercase;line-height:.95;letter-spacing:.01em}
.chip{display:inline-block;background:var(--chip_bg);color:var(--chip_fg);font-weight:700;font-size:30px;
      padding:12px 26px;border-radius:100px;letter-spacing:.06em;text-transform:uppercase}
p{font-size:42px;line-height:1.28;color:var(--sub)}
p b{color:var(--fg)}
.num{font-family:'Instrument Sans',sans-serif;font-weight:700;letter-spacing:-.04em;font-size:260px;line-height:.85;color:var(--acento)}
.rep{margin-top:34px;display:inline-flex;gap:16px;align-items:center;font-size:36px;font-weight:700;
     border:4px solid var(--fg);border-radius:100px;padding:14px 30px;align-self:flex-start}
.img{position:absolute;pointer-events:none}
.cmp{display:flex;flex-direction:column;gap:28px;margin-top:40px}
.cmp div{border-radius:28px;padding:30px 36px;font-size:38px;line-height:1.25}
.cmp .no{background:rgba(0,0,0,.08);border:3px dashed currentColor}
.cmp .si{background:var(--chip_bg);color:var(--chip_fg)}
.cmp span{display:block;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px;opacity:.85}
.lista{list-style:none;margin-top:36px;display:flex;flex-direction:column;gap:22px}
.lista li{font-size:40px;line-height:1.25;padding-left:58px;position:relative;color:var(--sub)}
.lista li:before{content:'';position:absolute;left:0;top:14px;width:30px;height:30px;border-radius:50%;background:var(--acento)}
.swipe{font-family:'Bebas Neue',sans-serif;font-size:44px;text-transform:uppercase;letter-spacing:.03em}
.aviso{font-size:24px;opacity:.75;margin-top:28px}
"""


def e(t):  # escapa y permite **negrita**
    t = html.escape(t)
    partes = t.split("**")
    return "".join(f"<b>{x}</b>" if i % 2 else x for i, x in enumerate(partes)).replace("\n", "<br>")


def pagina(tema, i, total, cuerpo, extra=""):
    v = TEMAS[tema]
    vars_ = ";".join(f"--{k}:{val}" for k, val in v.items())
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body style="{vars_}">{extra}
<div class="top"><span>FPROJECT · BAREFOOT</span><span class="n">{i:02d}/{total:02d}</span></div>
<div class="wrap">{cuerpo}</div>
<div class="foot"><span>@fproject_at</span><span>{'Desliza →' if i < total else 'Preventa · 15 oct'}</span></div>
</body></html>"""


def img(nombre, estilo):
    return f'<img class="img" src="../_img/{nombre}.png" style="{estilo}">'


# ---------- Contenido ----------
# Cada slide: (tema, tipo, datos)
CARRUSELES = {
"01-ejercicios-pies": [
    ("lima", "portada", dict(chip="Guía de fisio", titulo="Tus pies\ntienen +20\nmúsculos", sub="y la mayoría están **dormidos**.\n5 ejercicios para despertarlos.",
        imagen=("pies-separadores", "right:-150px;bottom:-60px;width:760px;-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 45%);mask-image:linear-gradient(to bottom,transparent 0%,#000 45%)"))),
    ("negro", "texto", dict(titulo="¿Por qué se\nduermen?", texto="Años de zapatos **rígidos**, con puntera **estrecha** y mucha amortiguación hacen el trabajo que le toca a tu pie.\n\nMúsculo que no se usa, **se debilita**.")),
    ("crema", "numero", dict(n="1", titulo="Pie corto", texto="Acerca la base del dedo gordo al talón **sin encoger los dedos**. El arco sube.", rep="10 reps × 5 seg")),
    ("crema", "numero", dict(n="2", titulo="Yoga de dedos", texto="Levanta **solo el dedo gordo** con los otros 4 apoyados. Luego al revés.\nAl principio cuesta. Es normal.", rep="10 de cada uno")),
    ("lima", "numero", dict(n="3", titulo="Abre los dedos", texto="Sepáralos lo más que puedas, sostén y relaja.\n**Con separadores es más fácil al inicio.**", rep="10 reps × 5 seg",
        imagen=("separador-flotando", "right:-60px;bottom:40px;width:520px;transform:rotate(18deg)"))),
    ("crema", "numero", dict(n="4", titulo="Talones lentos", texto="Sube en 2 seg, sostén 2 y baja en 4. Peso sobre el **dedo gordo**.", rep="3 series × 12")),
    ("crema", "numero", dict(n="5", titulo="Descalzo en casa", texto="10 minutos al día sobre superficies variadas. Tu pie **recibe información** en cada paso.", rep="Todos los días")),
    ("negro", "cta", dict(titulo="4 veces por semana.\n4 semanas.", texto="Y notarás la diferencia.", accion="Guárdalo para tu rutina", firma="Freddy Medina · Fisioterapeuta")),
],
"02-barefoot-vs-convencional": [
    ("rosa", "portada", dict(chip="Compara", titulo="Tu zapato\nvs tu pie", sub="**4 diferencias** que nadie\nte explicó.")),
    ("crema", "comparar", dict(n="1", titulo="La puntera", no="Estrecha y en punta. Aprieta los dedos.", si="Ancha, con la forma real del pie. Los dedos se abren.")),
    ("crema", "comparar", dict(n="2", titulo="El drop", no="Talón más alto que la punta: un mini tacón.", si="Cero drop. Talón y punta al mismo nivel, como descalzo.")),
    ("crema", "comparar", dict(n="3", titulo="La suela", no="Gruesa y rígida. No sientes el suelo.", si="Delgada y flexible. Tu pie siente y reacciona.")),
    ("crema", "comparar", dict(n="4", titulo="Quién trabaja", no="El zapato amortigua y sostiene por ti.", si="Tus músculos vuelven a trabajar.")),
    ("negro", "texto", dict(titulo="¿Tu zapato actual\nes malo?", texto="No. Tu pie **se acostumbró a no trabajar**.\n\nPor eso el cambio se hace **gradual**. Te lo explico en otro post.")),
    ("lima", "cta", dict(titulo="El pie no necesita\nmás tecnología.", texto="**Necesita libertad.**", accion="Comenta PREVENTA", firma="Preventa · 15 de octubre")),
],
"03-juanetes": [
    ("negro", "portada", dict(chip="Un fisio te explica", titulo="Juanetes:\n¿genética\no zapatos?", sub="",
        imagen=("pies-separadores", "right:-150px;bottom:-60px;width:720px;-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 45%);mask-image:linear-gradient(to bottom,transparent 0%,#000 45%)"))),
    ("crema", "texto", dict(titulo="¿Qué es un\njuanete?", texto="El **hallux valgus** es cuando el dedo gordo se desvía hacia los demás y aparece un **bulto en la base**.")),
    ("crema", "lista", dict(titulo="¿Por qué\naparece?", intro="Es **multifactorial**:", items=["Genética y forma del pie", "Laxitud de los ligamentos", "**Calzado estrecho y con tacón** que empuja el dedo día tras día"], cierre="La genética no la eliges. **El zapato, sí.**")),
    ("rosa", "lista", dict(titulo="Señales\nde alerta", intro="", items=["El dedo gordo **mira** hacia los otros", "Roce o enrojecimiento en la base", "Dolor al final del día con zapatos cerrados"], cierre="")),
    ("lima", "lista", dict(titulo="Qué puedes\nhacer hoy", intro="", items=["Zapatos con **puntera ancha**", "Yoga de dedos", "Separadores **10–20 min** al día", "Fortalece: pie corto y talones"], cierre="",
        imagen=("separador-flotando", "right:-80px;bottom:30px;width:480px;transform:rotate(-20deg)"))),
    ("negro", "texto", dict(titulo="Importante", texto="Ejercicios y separadores ayudan con la **movilidad**, las **molestias** y a que no empeore.\n\n**No borran** un juanete ya formado. Si hay dolor fuerte, consulta a un profesional.")),
    ("lima", "cta", dict(titulo="Guárdalo y\ncompártelo", texto="con esa persona que siempre\nse queja de sus juanetes.", accion="Envíaselo ahora", firma="Freddy Medina · Fisioterapeuta")),
],
"04-transicion-barefoot": [
    ("rosa", "portada", dict(chip="Antes de tu primer par", titulo="El error que\ntodos cometen\nal pasarse\nal barefoot", sub="(y cómo evitarlo)", tam=150)),
    ("negro", "texto", dict(titulo="El error", texto="Usarlos **todo el día desde el primer día**.\n\nTu pie lleva años sin trabajar. Si le pides todo de golpe, sobrecargas músculos, tendones y huesos.")),
    ("crema", "numero", dict(n="1–2", titulo="Semanas", texto="**1–2 horas al día**, en casa o caminando tranquilo.\n+ ejercicios de pie 3 veces por semana.", rep="Adaptación")),
    ("crema", "numero", dict(n="3–4", titulo="Semanas", texto="**Medio día** de uso. Caminatas más largas.\nNada de correr todavía.", rep="Progresión")),
    ("lima", "numero", dict(n="5–6", titulo="Semanas", texto="**Casi todo el día.** Empieza a entrenar con ellos: sentadilla, peso muerto, zancadas.", rep="Gimnasio")),
    ("crema", "numero", dict(n="7–8", titulo="Semanas", texto="**Uso completo.** Si corres, empieza con trotes cortos y aumenta poco a poco.", rep="Libertad")),
    ("negro", "comparar", dict(n="", titulo="Escucha a\ntu cuerpo", no="Dolor puntual en el hueso o que no se va: **para y consulta.**", si="Cansancio en pies y pantorrillas: normal, estás despertando músculos.", etiquetas=("Alerta", "Normal"))),
    ("lima", "cta", dict(titulo="Te acompañamos\nen la transición", texto="Guía completa de 8 semanas por DM.", accion="Comenta PREVENTA", firma="Preventa · 15 de octubre")),
],
}


def slide(tema, tipo, d, i, total):
    extra = img(*d["imagen"]) if d.get("imagen") else ""
    if tipo == "portada":
        cuerpo = f"""<div style="margin-top:-40px"><span class="chip">{e(d['chip'])}</span>
<h1 style="font-size:{d.get('tam',190)}px;margin-top:40px">{e(d['titulo'])}</h1>
<p style="margin-top:40px;max-width:{'560px' if extra else '900px'}">{e(d['sub'])}</p>
</div>"""
    elif tipo == "texto":
        cuerpo = f"""<h1 style="font-size:150px">{e(d['titulo'])}</h1><p style="margin-top:50px">{e(d['texto'])}</p>"""
    elif tipo == "numero":
        cuerpo = f"""<div class="num">{e(d['n'])}</div><h1 style="font-size:130px;margin-top:10px">{e(d['titulo'])}</h1>
<p style="margin-top:34px;max-width:{'560px' if extra else '900px'}">{e(d['texto'])}</p><div class="rep">↻ {e(d['rep'])}</div>"""
    elif tipo == "comparar":
        a, b = d.get("etiquetas", ("Convencional", "Barefoot"))
        pre = f'<div class="num" style="font-size:200px">{e(d["n"])}</div>' if d["n"] else ""
        cuerpo = f"""{pre}<h1 style="font-size:130px">{e(d['titulo'])}</h1>
<div class="cmp"><div class="no"><span>✕ {a}</span>{e(d['no'])}</div><div class="si"><span>✓ {b}</span>{e(d['si'])}</div></div>"""
    elif tipo == "lista":
        items = "".join(f"<li>{e(x)}</li>" for x in d["items"])
        intro = f'<p style="margin-top:36px">{e(d["intro"])}</p>' if d["intro"] else ""
        cierre = f'<p style="margin-top:40px">{e(d["cierre"])}</p>' if d["cierre"] else ""
        cuerpo = f"""<h1 style="font-size:140px">{e(d['titulo'])}</h1>{intro}<ul class="lista" style="max-width:{'640px' if extra else '900px'}">{items}</ul>{cierre}"""
    elif tipo == "cta":
        cuerpo = f"""<h1 style="font-size:140px">{e(d['titulo'])}</h1><p style="margin-top:36px">{e(d['texto'])}</p>
<div style="margin-top:60px"><span class="chip" style="font-size:40px;padding:22px 40px">{e(d['accion'])}</span></div>
<p style="margin-top:50px;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase">{e(d['firma'])}</p>
<p class="aviso">Contenido educativo. No reemplaza una valoración profesional.</p>"""
    return pagina(tema, i, total, cuerpo, extra)


lista = []
for nombre, slides in CARRUSELES.items():
    for i, (tema, tipo, d) in enumerate(slides, 1):
        f = OUT_HTML / f"{nombre}-{i:02d}.html"
        f.write_text(slide(tema, tipo, d, i, len(slides)), encoding="utf-8")
        lista.append({"html": str(f), "png": str(BASE / nombre / f"{i:02d}.png")})
        (BASE / nombre).mkdir(exist_ok=True)
(BASE / "_html" / "lista.json").write_text(json.dumps(lista, indent=1))
print(len(lista), "slides")
