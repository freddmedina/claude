# Contexto del proyecto: FProject (fprojectcompany)

Este archivo resume todo lo trabajado hasta ahora para que cualquier sesión nueva
de Claude pueda continuar sin volver a explicar el negocio. Idioma de trabajo: **español**.

## El negocio

- **Tienda Shopify:** fprojectcompany — dominio https://fprojectcompany.com
- **País / moneda / plan:** Colombia · COP · plan Basic
- **Fundador:** Freddy Medina, fisioterapeuta especializado en pie y movimiento
  (más de 6 años de práctica clínica y más de una década en entrenamiento funcional).
- **Enfoque:** calzado **barefoot** y salud del pie pensados desde la fisioterapia.
  En Colombia el barefoot es poco conocido, así que el contenido educativo es clave.
- **Tono de marca:** cercano, tuteando al lector, respaldado en fisioterapia.
  Frase de marca: "El pie no necesita más tecnología. Necesita libertad."
- La conexión de Claude con Shopify (conector MCP) funciona correctamente.

## Conexiones / herramientas (verificado 2026-10-03 con la lista de conectores MCP)
Conectores MCP conectados y activos: **Shopify, Windsor.ai, higgsfield, Gmail, Google Calendar, Calendly**.
No existe un conector MCP propio de Instagram: Instagram entra **a través de Windsor.ai**.
- **Shopify** (MCP): conectado a fprojectcompany (correo de la tienda: fprojectcompany26@gmail.com).
- **ElevenLabs** (MCP, conectado 2026-10-08): voces y locuciones (`creative_generate_speech`,
  `creative_list_voices`) y agentes de voz. Biblioteca con voces paisas/colombianas.
- **Higgsfield** (MCP): conectado · plan Plus · 1.000 créditos. Útil para fotos de producto,
  imágenes de los artículos del blog y videos/anuncios para redes. Aún no se ha usado.
- **Instagram** de la marca: https://www.instagram.com/fproject_at/ (@fproject_at).
  ✅ **Conectado vía Windsor.ai (MCP)** — verificado 2026-10-03. Cuenta Windsor: plan **Trial** (gratis).
  - Instagram account ID en Windsor: `17841469436603089` (conector `instagram`).
  - **Lectura de métricas** (`get_data`): perfil (seguidores, bio, enlace), alcance, vistas,
    interacciones, nuevos seguidores por día, métricas por publicación/reel/historia y audiencia.
  - **Acciones de escritura** (`execute_action`, siempre con confirmación de Fredd): publicar imagen,
    carrusel, video/reel e historia; responder, ocultar o borrar comentarios.
  - Línea base (27/09–03/10/2026): 707 seguidores, 668 seguidos, 27 publicaciones,
    ~3.373 vistas y 88 interacciones en 7 días, +9 seguidores. Bio aún apunta al Linktree personal.

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

- Blog de Shopify: título **"Blogs"**, handle `news` (`gid://shopify/Blog/124274704753`), URLs `/blogs/news/{handle}`.
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

## Pie de página (footer)

- Tema activo: **"Tinker - Bebas Neue"** (`gid://shopify/OnlineStoreTheme/198768656753`).
  Las columnas del footer son bloques de menú en `sections/footer-group.json`.
  El conector no puede editar archivos del tema activo; esos cambios se hacen en el editor de temas.
- Menús creados/actualizados en Navegación:
  - `footer` (columna **Shop**): Barefoot KIBA PROJECT + Separadores de dedos.
  - `footer-help` (columna **Help**): enlace `mailto:fprojectcompany26@gmail.com`.
  - `footer-about` (columna **About**): "Quiénes somos" → `/pages/contact`.
- ✅ Verificado 2026-10-03: Help → `footer-help`, About → `footer-about`, Stay Connected → solo
  Instagram `https://www.instagram.com/fproject_at/` (Facebook/TikTok/X eliminados).
- Los títulos del footer y el newsletter siguen en inglés ("Shop", "Help", "About", "Stay Connected").
  Según la rama `claude/ecstatic-wright-ae4ujb`, la web mitad español / mitad inglés es una
  **decisión de marca a propósito** (30/09/2026): no traducirlos sin preguntar.

## Finanzas (actualizado 2026-10-08)
- **Regla:** toda conversación financiera o contable con Freddy la responde **Angela** en primera
  persona (cargar el skill `gerente-financiero`; para libros e impuestos, Angela se apoya en el
  skill `contador`). Si Freddy le habla a "Angela", responder como ella aunque el tema no sea
  financiero. Audio con la voz de Lina solo cuando Freddy lo pida.
- Skill **`gerente-financiero`** (`.claude/skills/gerente-financiero/`): CFO del negocio, persona
  **Angela** con voz ElevenLabs "Lina" paisa (`yfUfwZTRubVrsUZWqzwp`, modelo `eleven_v3`). Su
  línea base, mapa del Excel `fproject_ecommerce.xlsx` y errores detectados están en
  `references/estado-financiero.md`; notas tributarias Colombia en `references/colombia-tributario.md`.
- Datos clave: costo aterrizado KIBA **112.162 COP/par** (750 pares, FOB USD 19,58, TRM 3.493,
  pedido total 84,1 M). Shopify cobra **IVA 19% incluido** (480.000 → 403.361 neto).
  Contribución KIBA antes de pauta ≈ 250.000/par. Costos fijos ≈ 2,76 M/mes (sin sueldo ni contador).
- Skill **`contador`** (`.claude/skills/contador/`): contador interno del equipo de Angela. Lleva la
  contabilidad en `contabilidad/` (libro diario, kardex, cierres) y arma el paquete contable que se
  envía al **contador externo** solo cuando hay que presentar una declaración. El externo solo hace
  renta y presentaciones puntuales, y cobra por presentación.
- Freddy factura como **persona natural**. Todas las ventas (incluida familia y amigos) se registran
  en Shopify. La mercancía KIBA llega ~**15 nov 2026** ya nacionalizada.
- Ventas reales en Shopify a 2026-10-08: solo 4 separadores, **0 pares KIBA**. Inventario KIBA en
  Shopify: 762 pares (ubicación "envia ff bogota"), tallas 45 con 4 por color.

## Pendientes / ideas siguientes
- [ ] Freddy revisa y publica los 8 borradores.
- [ ] Decidir nombre del blog (antes de publicar).
- [ ] Decidir si traducir colores de variantes (Green/Yellow/Black → Verde/Amarillo/Negro).
- [ ] Posibles artículos nuevos: "pie plano", "ejercicios para fortalecer los pies".
- [ ] Revisar reposición de inventario en tallas 44 y 45.
