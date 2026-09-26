# Contexto del proyecto: FProject (fprojectcompany)

Este archivo resume todo lo trabajado hasta ahora para que cualquier sesión nueva
de Claude pueda continuar sin volver a explicar el negocio. Idioma de trabajo: **español**.

## El negocio

- **Tienda Shopify:** fprojectcompany — dominio https://fprojectcompany.com
- **País / moneda / plan:** Colombia · COP · plan Basic
- **Fundador:** **Fredd Medina** (así se escribe su nombre en todo: correos, firmas, artículos),
  fisioterapeuta especializado en pie y movimiento, con **13 años pasando consulta**
  (y más de una década en entrenamiento funcional).
- **Enfoque:** calzado **barefoot** y salud del pie pensados desde la fisioterapia.
  En Colombia el barefoot es poco conocido, así que el contenido educativo es clave.
- **Tono de marca:** cercano, tuteando al lector, respaldado en fisioterapia.
  Frase de marca: "El pie no necesita más tecnología. Necesita libertad."
- La conexión de Claude con Shopify (conector MCP) funciona correctamente.

## Datos de la tienda (verificados con `get-shop-info` el 2026-09-26)

| Campo | Valor |
|---|---|
| Nombre | fprojectcompany |
| Dominio | fprojectcompany.com |
| Email de la tienda | fprojectcompany26@gmail.com |
| Plan | Basic |
| Moneda | COP |
| País | Colombia |
| Zona horaria | **EDT** (hora del este de EE. UU.) ⚠️ |

- ⚠️ **Zona horaria incorrecta:** la tienda está en EDT y no en hora de Bogotá (COT, UTC-5).
  Entre abril y noviembre hay 1 hora de diferencia, lo que afecta fechas de pedidos,
  informes y la hora de publicación programada de los artículos del blog.
  Se corrige en Shopify → *Configuración → General → Zona horaria*. Pendiente que Fredd lo cambie.

## Repositorio y herramientas de trabajo

- Repositorio GitHub: `freddmedina/claude` (contiene este `CLAUDE.md` como memoria del proyecto).
- Ramas: `claude/great-brown-6fb6cj` (rama de trabajo actual) y
  `claude/shopify-connection-check-3grq00` (sesión de verificación de conexión; al
  2026-09-26 tenía el mismo contenido que la rama de trabajo, commit `9bfc6b4`).
- Conectores MCP disponibles en las sesiones: **Shopify** (productos, inventario, pedidos,
  clientes, colecciones, descuentos, analítica y GraphQL Admin para blogs/metafields),
  **GitHub**, **Claude Docs** y **Higgsfield** (generación de imágenes/video, útil para
  imágenes de artículos o contenido de redes).
- Mantener este archivo actualizado al final de cada sesión con lo que se haya hecho.

## Productos

### 1. KIBA PROJECT - BAREFOOT (zapatos)
- URL: `/products/barefoot` · ID: `gid://shopify/Product/15506559893873`
- Precio: 480.000 COP · Estado: activo
- Características: suela flexible, cero drop, diseño anatómico, puntera ancha.
  Para gimnasio y uso diario.
- **Incluye plantilla de transición:** da algo más de soporte mientras el pie se adapta;
  al quitarla se tiene la **experiencia barefoot completa**. Mencionarlo siempre que se
  hable de transición o se presente el producto (correos, artículos, fichas).
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
  Su autor en Shopify figura como **"Mandala Cases"** (pendiente confirmar si se cambia a Fredd Medina).
  En su texto se corrigió "Freddy" → "Fredd Medina" (2026-09-26).

### 8 artículos creados como BORRADOR (pendientes de revisión de Fredd)

Autor en Shopify: **Fredd Medina** (corregido el 2026-09-26). Cada uno tiene meta título y meta descripción (metafields
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

Estudios citados en los artículos (Fredd debe validarlos): Ridge et al. 2019 (fuerza del pie
con calzado minimalista), Ridge et al. 2013 (estrés óseo por transición rápida),
Lieberman et al. 2010 (pisada al correr descalzo), Rathleff et al. 2015 (ejercicio de fuerza
en fascitis plantar).

### Recomendaciones dadas
- Publicar 1–2 artículos por semana en lugar de todos juntos.
- Publicar en grupos completos: mientras un artículo siga en borrador, los enlaces hacia él
  desde los ya publicados no funcionan.
- Reemplazar imágenes por fotos propias por tema cuando sea posible y añadir anécdotas clínicas.

## Identidad visual (tomada del tema activo "Tinker", `config/settings_data.json`)

| Elemento | Archivo / valor | URL |
|---|---|---|
| **Logo oficial horizontal, oscuro** (fondos claros) — USAR SIEMPRE | `logo-fproject-oscuro.png` (1200×340, transparente, gris `#353535`) | https://cdn.shopify.com/s/files/1/1004/6446/0145/files/logo-fproject-oscuro.png?v=1790444598 |
| **Logo oficial horizontal, blanco** (fondos oscuros) — USAR SIEMPRE | `logo-fproject-blanco.png` (1200×340, transparente) | https://cdn.shopify.com/s/files/1/1004/6446/0145/files/logo-fproject-blanco.png?v=1790444598 |
| Logo del tema (web, fondos claros) | `Diseno_sin_titulo_1.png` (1000×1000) | https://cdn.shopify.com/s/files/1/1004/6446/0145/files/Diseno_sin_titulo_1.png |
| Logo inverso del tema (web) | `4.png` (1000×1000) | https://cdn.shopify.com/s/files/1/1004/6446/0145/files/4.png |
| Favicon | `3.png` (475×475) | https://cdn.shopify.com/s/files/1/1004/6446/0145/files/3.png |

- **Logo oficial** (entregado por Fredd el 2026-09-26): isotipo "F" en líneas + "PROJECT" +
  "THERAPY · MOVEMENT · TRAINING". Vectorial corregido en `marca/logo-fproject.pdf`
  (el original de Illustrator decía "THERAPHY" y se guarda como `marca/logo-fproject-original-theraphy.pdf`);
  PNG en `marca/logo-fproject-oscuro.png` y `marca/logo-fproject-blanco.png`, también subidos
  a Shopify → Contenido → Archivos (IDs `gid://shopify/MediaImage/70412684067185` y `...70412684099953`).
  Usarlo en correos, piezas gráficas y cualquier material donde se necesite el logo.
- Ortografía corregida a "THERAPY" (2026-09-26): se quitó la H sobrante y se repartió el espacio para
  que el lema siga alineado con "PROJECT". Si hay otros materiales impresos o redes con "THERAPHY", actualizarlos.

- **Colores:** verde salvia `#c3cca6` (botones principales), negro `#000000` (texto, bordes),
  blanco `#ffffff`, crema `#faf9f1` y `#f1ede7` (fondos), verde hover `#82a31a`,
  gris borde `#e6e6e6`.
- **Tipografías:** títulos **Bayon** (en mayúsculas), texto **Instrument Sans**, acento Radio Canada Big.
- **Botones:** fondo `#c3cca6`, texto negro, borde negro de 1px, bordes redondeados (píldora).
- Nota técnica: desde las sesiones en la nube el CDN de Shopify está bloqueado por red,
  así que Claude no puede ver las imágenes. Los logos del tema se identificaron por su configuración; el logo oficial se revisó a partir del PDF.

## Correos y newsletter

- En la web hay un formulario de newsletter ("ofertas e información"). Los suscriptores quedan
  como clientes con `email_marketing_state: subscribed`. Al 2026-09-26 había **1 suscriptor**.
- Se envía desde Shopify Messaging (Shopify Email), con el remitente de la tienda
  (fprojectcompany26@gmail.com).

### Guía de tono para TODOS los correos
- Escribe Fredd en primera persona, tuteando, cercano y cálido ("¡Hola! 👋", "Un abrazo").
- Respaldo en fisioterapia: mencionar la experiencia clínica y explicar el porqué, sin sonar técnico.
- Educar antes de vender: en Colombia el barefoot es poco conocido.
- Emojis con moderación (👋 🦶 🏋️ 🎁 👣), uno por idea como máximo.
- Siempre: logo oficial oscuro arriba, frase de marca "El pie no necesita más tecnología. Necesita libertad.",
  firma "Fredd Medina · Fisioterapeuta · Fundador de FProject", logo oficial blanco en el pie
  y el aviso "El contenido tiene fines educativos y no reemplaza una valoración profesional".
- Invitar a responder el correo ("Responde este correo y te leo personalmente").
- Enlazar solo a páginas publicadas (no a artículos en borrador).

### Correo de bienvenida al newsletter (plantilla lista)
- Archivo: `correos/bienvenida-newsletter.html` (HTML de correo con logos, colores y tipografías de marca).
- **Asunto:** Bienvenido a FProject: tus pies te lo van a agradecer 👣
- **Preheader:** Gracias por unirte. Te cuento qué vas a recibir y por dónde empezar.
- **Estructura:** logo → franja salvia con título "BIENVENIDO A LA COMUNIDAD FPROJECT" y la frase de marca →
  saludo y presentación de Fredd → "¿Qué vas a recibir?" (contenido de fisio, ejercicios, ofertas
  anticipadas) → botón a "¿Qué es el calzado barefoot?" → tarjetas de KIBA Barefoot y separadores →
  consejo de transición gradual + plantilla de transición de los KIBA (al quitarla, experiencia barefoot
  completa) → firma → pie negro con logo blanco y aviso educativo. Presentación: "13 años pasando consulta".
- Sin descuento por ahora. Si Fredd quiere uno (ej. `BIENVENIDA10`), crearlo en Shopify y añadirlo al correo.

### Cómo se activa el envío automático (lo hace Fredd en el admin de Shopify)
La API no permite crear automatizaciones de marketing, así que se configura a mano:
1. Admin de Shopify → **Marketing → Automatizaciones** → **Crear automatización**.
2. Elegir la plantilla **"Dar la bienvenida a nuevos suscriptores"**
   (disparador: *el cliente se suscribió al marketing por correo*).
3. Editar el correo del flujo: asunto y preheader de arriba. Si el editor tiene la sección
   **"Liquid personalizado"/código**, pegar el HTML de `correos/bienvenida-newsletter.html`;
   si no, armarlo con los bloques del editor usando los mismos textos, logo y colores.
4. Enviar una prueba al propio correo, revisarla en el celular y **activar** la automatización.
5. Verificar: suscribirse con un correo de prueba desde la web y confirmar que llega.

### Aviso de artículos nuevos a los suscriptores
- Shopify **no** tiene un disparador automático "se publicó un artículo → enviar correo a la lista",
  y la API no permite crear ni enviar campañas de Shopify Messaging.
- Opciones analizadas (2026-09-26):
  1. **Campaña manual en Shopify Messaging** por cada artículo (o un resumen semanal), con una plantilla
     fija "Nuevo artículo" que prepara Claude. Gratis dentro del cupo de Shopify, unos 5 minutos por envío.
  2. **Automático con una app de email (Mailchimp o Klaviyo)** leyendo el feed del blog
     `https://fprojectcompany.com/blogs/news.atom`: envía solo cuando sale un artículo nuevo.
     Requiere instalar la app, sincronizar los suscriptores y revisar el costo del plan.
- Cambios en artículos (2026-09-26): en `zapatos-barefoot-en-colombia-como-elegir` se cambió
  "más de 6 años de práctica clínica" por "13 años pasando consulta" y se añadió la plantilla de transición
  a las características de KIBA.

## Pendientes / ideas siguientes
- [ ] Fredd revisa y publica los 8 borradores.
- [ ] Decidir nombre del blog (antes de publicar).
- [ ] Decidir si traducir colores de variantes (Green/Yellow/Black → Verde/Amarillo/Negro).
- [ ] Posibles artículos nuevos: "pie plano", "ejercicios para fortalecer los pies".
- [ ] Revisar reposición de inventario en tallas 44 y 45.
- [ ] Cambiar la zona horaria de la tienda de EDT a Bogotá (COT).
- [ ] Activar la automatización del correo de bienvenida del newsletter en Shopify.
- [ ] Decidir si el correo de bienvenida lleva un código de descuento.
- [x] Cambiar el autor de los 8 borradores a "Fredd Medina".
- [x] Corregir el logo a "THERAPY".
- [ ] Decidir cómo avisar a los suscriptores cuando se publica un artículo (ver "Aviso de artículos nuevos").
- [ ] Revisar las fotos de marca con "THERAPHY" (redes, empaques, material impreso).

## Historial de sesiones
- **Sesión inicial:** sistema de SKU aplicado, 8 artículos del blog creados como borrador,
  creación de este `CLAUDE.md`.
- **2026-09-26:** verificada la conexión con Shopify (OK). Se detectó la zona horaria en EDT.
  Se revisó la rama `claude/shopify-connection-check-3grq00` (sin cambios frente a la rama de trabajo).
  Se identificaron logos, colores y tipografías del tema, y se creó el correo de bienvenida del
  newsletter (`correos/bienvenida-newsletter.html`) con su guía de tono y pasos de activación.
  Correcciones de Fredd: nombre "Fredd Medina", 13 años pasando consulta, mención de la plantilla
  de transición de los KIBA, y logo oficial (PDF) convertido a PNG y subido a Shopify.
