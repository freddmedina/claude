# Contexto del proyecto: FProject (fprojectcompany)

Este archivo resume todo lo trabajado hasta ahora para que cualquier sesión nueva
de Claude pueda continuar sin volver a explicar el negocio. Idioma de trabajo: **español**.

## El negocio

- **Tienda Shopify:** fprojectcompany — dominio https://fprojectcompany.com
- **País / moneda / plan:** Colombia · COP · plan Basic
- **Fundador:** Freddy Medina (firma pública en contenido: **"Fredd Medina"**), fisioterapeuta especializado en pie y movimiento
  (más de 6 años de práctica clínica y más de una década en entrenamiento funcional).
- **Enfoque:** calzado **barefoot** y salud del pie pensados desde la fisioterapia.
  En Colombia el barefoot es poco conocido, así que el contenido educativo es clave.
- **Tono de marca:** cercano, tuteando al lector, respaldado en fisioterapia.
  Frase de marca: "El pie no necesita más tecnología. Necesita libertad."
- La conexión de Claude con Shopify (conector MCP) funciona correctamente.

## Productos

### 1. KIBA PROJECT - BAREFOOT (zapatos)
- URL: `/products/barefoot` · ID: `gid://shopify/Product/15506559893873`
- Precio: 480.000 COP · Estado: activo
- Características: suela flexible, cero drop, diseño anatómico, puntera ancha.
  Para gimnasio y uso diario.
- 30 variantes: tallas **36 a 45** × colores **Green / Yellow / Black**
  (los nombres de color están en inglés en Shopify; está pendiente decidir si se traducen).
- Inventario bajo en tallas 44 (5 por color) y 45 (4 por color).

### 2. Separadores de dedos en silicona médica (marca F Movement)
- URL: `/products/separadores-de-dedos-en-silicona-medica` · ID: `gid://shopify/Product/15506533745009`
- Precio: 40.000 COP · 1 variante (talla única) · Estado: activo
- Silicona médica hipoalergénica, reutilizable, incluye caja con guía ilustrada de uso y ejercicios.

## Sistema de SKU (ya aplicado en Shopify)

Formato: `FP-{PRODUCTO}-{COLOR/MATERIAL}-{TALLA}`

| Producto | Formato | Ejemplo |
|---|---|---|
| Zapatos KIBA | `FP-KIBA-{VER\|AMA\|NEG}-{36..45}` | `FP-KIBA-NEG-40` = negro talla 40 |
| Separadores | `FP-SEP-SIL-U` | silicona, talla única |

- `FP` = fprojectcompany · `VER` = verde · `AMA` = amarillo · `NEG` = negro · `U` = talla única.
- Para productos nuevos seguir el mismo patrón (ej. `FP-KIBA2-...`, `FP-SEP-SIL-M`).
- Las tallas 36 y 37 tenían SKU antiguos que se reemplazaron:
  `GREEN-INF-3x` → `FP-KIBA-VER-3x`, `YELLOW-VANILLA-3x` → `FP-KIBA-AMA-3x`,
  `NEG-PHANTON-3x` → `FP-KIBA-NEG-3x`. Si se usaban en otro lado, habría que revertir.

## Blog y SEO

- Blog de Shopify: **"News"** (`gid://shopify/Blog/124274704753`), URLs `/blogs/news/{handle}`.
  Pendiente: si se quiere renombrar (ej. "Blog" o "Aprende barefoot"), hacerlo ANTES de publicar
  los borradores para no romper los enlaces internos.
- Artículo ya **publicado** (previo): "¿Qué es el calzado barefoot?" — `que-es-el-calzado-barefoot`.

### 8 artículos creados como BORRADOR (pendientes de revisión de Freddy)

Autor: Freddy Medina. Cada uno tiene meta título y meta descripción (metafields
`global.title_tag` / `global.description_tag`), resumen, etiquetas, imagen con alt,
sección de preguntas frecuentes, aviso de fines educativos y enlaces internos entre
artículos y hacia los productos.

| # | Handle | Tema / palabra clave |
|---|---|---|
| 1 | `beneficios-del-calzado-barefoot-para-la-salud` | beneficios calzado barefoot |
| 2 | `como-hacer-la-transicion-al-calzado-barefoot` | transición barefoot (plan 8 semanas) |
| 3 | `zapatos-barefoot-vs-zapatos-convencionales` | barefoot vs convencional, zero drop |
| 4 | `zapatos-barefoot-en-colombia-como-elegir` | zapatos barefoot Colombia, guía de tallas |
| 5 | `juanetes-hallux-valgus-causas-ejercicios-y-calzado` | juanetes / hallux valgus |
| 6 | `fascitis-plantar-y-calzado-barefoot` | fascitis plantar |
| 7 | `separadores-de-dedos-para-que-sirven` | separadores de dedos |
| 8 | `zapatos-barefoot-para-gimnasio-y-entrenamiento` | zapatos para gimnasio, sentadilla, crossfit |

Estudios citados en los artículos (Freddy debe validarlos): Ridge et al. 2019 (fuerza del pie
con calzado minimalista), Ridge et al. 2013 (estrés óseo por transición rápida),
Lieberman et al. 2010 (pisada al correr descalzo), Rathleff et al. 2015 (ejercicio de fuerza
en fascitis plantar).

### Recomendaciones dadas
- Publicar 1–2 artículos por semana en lugar de todos juntos.
- Publicar en grupos completos: mientras un artículo siga en borrador, los enlaces hacia él
  desde los ya publicados no funcionan.
- Reemplazar imágenes por fotos propias por tema cuando sea posible y añadir anécdotas clínicas.

## Identidad visual (tema Shopify "Tinker")

- Tipografías: títulos **Bebas Neue** (`bebas_neue_n4`), texto **Instrument Sans**, acento **Radio Canada Big**.
  Antes era **Bayon**, que no tiene tildes ni ñ.
- **Tema publicado (desde 28/09/2026): "Tinker - Bebas Neue"** (`gid://shopify/OnlineStoreTheme/198768656753`).
  Verificado por API: idéntico al anterior salvo la fuente de títulos en `config/settings_data.json`.
  Respaldo: tema **"Tinker"** (`192220201329`, sin publicar, con Bayon). También existe "Horizon" sin usar.
  Claude NO puede escribir ni publicar en el tema en vivo (la API lo bloquea): para cambios, duplicar el tema,
  editar la copia y que Freddy la publique. Para archivos grandes: stagedUploadsCreate (FILE, PUT) + subir con curl
  + themeFilesUpsert con body type URL = resourceUrl (funciona; verificar checksumMd5). Hay una actualización del tema (v4.2.0) disponible, sin aplicar.
- Paleta de la web:
  - Negro `#000000` / Blanco `#FFFFFF` (base, texto y botones hover)
  - Verde salvia `#C3CCA6` (botón principal, color protagonista)
  - Verde oliva `#82A31A` (hover de enlaces)
  - Crema claro `#FAF9F1` y arena `#F1EDE7` (fondos cálidos)
  - Dorado arena `#D3B571` (bloque destacado)
  - Naranja suave `#FFAA62` y mostaza `#FDC656` (acentos)
  - Verde grisáceo `#68807E` (botón secundario)
- Paleta real de Instagram (distinta a la web, más "street/energía"): verde lima neón `#B8F03C`,
  degradados rosa-magenta `#F45BC6` → naranja `#FF9A4A`, morado, fotos en blanco y negro y fondo negro.
  Ilustraciones estilo cartoon, titulares grandes en mayúsculas.
- Videos de separadores (Higgsfield) con fondo cambiado en `contenido/videos-separadores/`
  (versiones lima, rosa-naranja y salvia). Se hizo recortando el fondo gris con código, sin gastar
  créditos; editarlos con Seedance 2.5 costaba 46 créditos por video a 720p.
- Instagram: **@fproject_at** (https://www.instagram.com/fproject_at/). Objetivo actual:
  crecimiento orgánico antes de invertir en ads; en el lanzamiento habrá más video.
- Higgsfield: plan Plus (56 créditos al 27/09/2026). Desde Claude no se puede abrir
  Instagram ni descargar imágenes (bloqueo de red); hay que subir las artes al chat
  o a Higgsfield para trabajarlas.

## Lanzamiento

- **Lanzamiento con preventa: 15 de octubre de 2026.** La web fprojectcompany.com aún no está
  abierta al público (por eso la bio apunta al Linktree personal por ahora).
- Mucha gente ya conoce los zapatos. Antes del lanzamiento, la idea es activar la cuenta
  para ganar seguidores con Reels cortos y carruseles educativos.
- Plan de prelanzamiento (29 sep a 14 oct) con 4 carruseles, 2 Reels de separadores, historias
  y plantillas de DM: `contenido/plan-prelanzamiento-instagram.md`.
  Llamados: "Comenta PREVENTA" (lista de espera) y "Comenta SEPARADOR".
- **Carruseles diseñados** (4 carruseles, 30 slides PNG 1080×1350) en `contenido/carruseles/`:
  01 ejercicios de pies · 02 barefoot vs convencional · 03 juanetes · 04 transición.
  Se generan con `python3 contenido/carruseles/generar.py && node contenido/carruseles/render.js`
  (textos en `generar.py`; fuentes Bebas Neue (títulos) + Instrument Sans locales; Bayon NO tiene tildes ni ñ; paleta lima/negro/crema/rosa-naranja;
  recortes del separador en `_img/`). Para cambiar un texto: editar `generar.py` y volver a correr.
- Prompts de video para Higgsfield (2): `contenido/prompts-videos-separadores.md`.
  Costos: Seedance 2.0 fast 15 créditos / Seedance 2.5 42 créditos por video de 6 s a 720p.
- Pendiente: diseñar la estrategia de campaña del lanzamiento.

## Instagram @fproject_at — diagnóstico (27/09/2026, a partir de pantallazos)

**Perfil**
- 24 publicaciones · 702 seguidores · 684 seguidos (relación casi 1:1, se lee como "sígueme y te sigo").
- Nombre: "Fproject® | Barefoot" · Categoría: "Sitio web de salud y bienestar".
- Bio: "by @freddmedinaft (fisioterapeuta) / Una marca creada para devolverle vida a tus pies 🦶 /
  Mira nuestros productos aquí ⬇️".
- Enlace: `linktr.ee/freddmedinaft` (el Linktree personal de Freddy, NO la tienda) + Threads.
- Destacadas: solo 1 ("espaciadores").
- Cuenta personal de Freddy: @freddmedinaft.

**Contenido publicado (cuadrícula)**
- Educativos: "Datos sobre tus pies que nadie te contó", "3 mitos sobre el barefoot",
  "principios de percepción sensorial", "Tus pies nacen así", "La industria del calzado te mintió",
  "Tu cuerpo envía mensajes a través de cada pisada", "Ellos quieren que no sientas nada /
  nosotros queremos que sientas todo", "La verdad sobre el grounding".
- Personas: Reel "El origen de FProject" (Freddy), Reel "Conoce Infinity" (otra persona).
- Ilustraciones estilo cartoon (zapatos verdes, corredora, personaje con pie grande).
- Producto: foto de cajas F Movement con separadores.
- Varios copys en inglés: "Barefoot isn't a trend…", "Never done being obsessed with your feet",
  "Don't be the last to wake up", "Human evolution 2026".
- Estética: verde lima neón, degradados rosa/magenta/naranja, morado, fotos en blanco y negro,
  fondo negro, titulares grandes en mayúsculas.

**Métricas de referencia — post "La verdad sobre el grounding" (carrusel ilustrado)**
| Métrica | Valor |
|---|---|
| Visualizaciones | 512 (60,4 % seguidores / 39,6 % no seguidores) |
| Origen | Inicio 299 · Otro origen 171 · Perfil 42 |
| Espectadores (cuentas alcanzadas) | 254 (~36 % de los seguidores) |
| Interacciones | 25 → 17 me gusta · 1 compartido · 0 comentarios · 0 guardados |
| Cuentas con interacciones | 17 |
| Actividad en el perfil | 6 → 5 visitas · 0 toques en enlace · 1 seguidor nuevo |

**Problemas detectados**
1. 0 guardados y 0 comentarios: el contenido gusta pero no se guarda ni genera conversación.
2. 0 toques en el enlace: la bio manda al Linktree personal, no a fprojectcompany.com.
3. Mezcla de inglés y español; público colombiano.
4. Poco producto real en uso (KIBA casi no aparece puesto) y poca cara de Freddy como fisio.
5. Textos cortados en la cuadrícula (recorte 3:4).
6. Paleta de Instagram distinta a la web.
7. Nombre del zapato inconsistente: "Infinity" en IG vs "KIBA PROJECT" en la tienda → decidido: **KIBA**.
8. Temas como "grounding" tienen poca evidencia: cuidar la credibilidad de fisioterapeuta.

## Pendientes / ideas siguientes
- [ ] Freddy revisa y publica los 8 borradores.
- [ ] Decidir nombre del blog (antes de publicar).
- [ ] Decidir si traducir colores de variantes (Green/Yellow/Black → Verde/Amarillo/Negro).
- [ ] Posibles artículos nuevos: "pie plano", "ejercicios para fortalecer los pies".
- [ ] Revisar reposición de inventario en tallas 44 y 45.
- [ ] Instagram: al abrir la web (15 oct) cambiar enlace de bio a la tienda; ya: categoría a "Marca de ropa/calzado", reescribir bio.
- [ ] Instagram: pasar copys a español; usar siempre KIBA como nombre del zapato.
- [ ] Instagram: crear destacadas (Qué es barefoot, Tallas, Transición, Opiniones, Envíos).
- [x] Publicar el tema "Tinker - Bebas Neue" (hecho y verificado el 28/09).
- [x] **Nombre del zapato: KIBA** (decidido 28/09; ya no usar "Infinity" como nombre del modelo).
- [ ] Publicar el tema **"Tinker - KIBA en español"** (`gid://shopify/OnlineStoreTheme/198780649841`): copia del tema
  en vivo con portada y pie de página en español. Cambios: "Introducing KIBA"→"Conoce KIBA";
  "MOVE FREELY. LIVE INFINITY."(×2)→"MUÉVETE LIBRE. VIVE SIN LÍMITES."; "Bestsellers"→"Los más vendidos";
  "Shop Now"(×2)→"Comprar ahora"; footer: newsletter→"Únete a la comunidad FProject: novedades, ofertas y acceso
  anticipado.", "Sign up"→"Suscribirme", "Shop/Help/About"→"Tienda/Ayuda/Nosotros", "Stay Connected"→"Síguenos".
- [ ] Decidir nombres de colorway en la sección "Tres imágenes con texto" (PHANTON / INFINITY / VANILLA VIBE)
  y "Rising Yellow"; "PHANTON" parece error de "PHANTOM". Los colores en Shopify son Green/Yellow/Black.
- [ ] Unificar paleta web + Instagram.
- [ ] Estrategia de campaña de lanzamiento (preventa 15 oct).
