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
  Se corrige en Shopify → *Configuración → General → Zona horaria*. Pendiente que Freddy lo cambie.

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

## Pendientes / ideas siguientes
- [ ] Freddy revisa y publica los 8 borradores.
- [ ] Decidir nombre del blog (antes de publicar).
- [ ] Decidir si traducir colores de variantes (Green/Yellow/Black → Verde/Amarillo/Negro).
- [ ] Posibles artículos nuevos: "pie plano", "ejercicios para fortalecer los pies".
- [ ] Revisar reposición de inventario en tallas 44 y 45.
- [ ] Cambiar la zona horaria de la tienda de EDT a Bogotá (COT).

## Historial de sesiones
- **Sesión inicial:** sistema de SKU aplicado, 8 artículos del blog creados como borrador,
  creación de este `CLAUDE.md`.
- **2026-09-26:** verificada la conexión con Shopify (OK). Se detectó la zona horaria en EDT.
  Se revisó la rama `claude/shopify-connection-check-3grq00` (sin cambios frente a la rama de trabajo).
