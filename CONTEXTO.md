# Contexto de trabajo — fprojectcompany (KIBA)

Resumen para retomar en otra conversación con Claude. Última actualización: 2026-10-01.

## Conexiones

| Servicio | Estado | Datos clave |
|---|---|---|
| Shopify | Conectado | Tienda `fprojectcompany` (fprojectcompany.com) · Plan Basic · COP · Colombia (UTC−05) |
| Higgsfield | Conectado | Plan Plus · workspace privado `e20611c3-3377-4fb2-b90b-cd26f82a2fa8` (ya seleccionado) · ~56 créditos tras los 2 videos |
| GitHub | Repo `freddmedina/claude`, rama `claude/sleepy-ritchie-ptcpxp` | Estaba vacío; este archivo es el primer commit |

## Productos relevantes (Shopify)

- **Separadores de dedos en silicona médica** — `gid://shopify/Product/15506533745009`
  - handle: `separadores-de-dedos-en-silicona-medica` · SKU `FP-SEP-SIL-U` · $40.000 COP · 1 variante · ~296 unidades
- **Barefoot** — `gid://shopify/Product/15506559893873` (handle `barefoot`)
  - Colores mostrados en el inicio: PHANTON, INFINITY, VANILLA VIBE

## Temas de Shopify

| Tema | ID | Rol |
|---|---|---|
| Tinker - KIBA en español | `198780649841` | **MAIN (publicado)** |
| **Tinker - Bebas Neue** | `198768656753` | Sin publicar — **es el tema que el equipo decidió usar** |
| Tinker | `192220201329` | Sin publicar |
| Horizon | `192220168561` | Sin publicar |

Nota: por la API solo se pueden editar archivos de temas **no publicados**. Publicar el tema se hace desde el admin de Shopify.

### Decisión de idioma
El equipo decidió mantener la página **mitad español, mitad inglés**. Textos en inglés como "Shop Now", "Bestsellers", "MOVE FREELY. LIVE INFINITY." e "Introducing KIBA" se mantienen.

## Cambios hechos en "Tinker - Bebas Neue"

1. **ARTÍCULOS → BLOGS**
   - `templates/index.json`: título de las dos secciones de blog cambiado de `{{ closest.blog.title }}` a `BLOGS`.
   - `templates/blog.json`: título de la página del blog cambiado a `BLOGS`.
2. **Bloque de color en el inicio** (`templates/index.json`, sección `media_with_content_LfPdEJ`)
   - Título: `RISING YELLOW = LIBERTAD` → `VANILLA VIBE = LIBERTAD`
   - Descripción: "Nuestro Rising Yellow simboliza…" → "Nuestro Vanilla Vibe simboliza el impulso de avanzar, explorar y descubrir nuevos caminos. Un color inspirado en quienes nunca dejan de moverse."
3. **Guía de tallas en separadores** (`blocks/ai_gen_block_12ac997.liquid`)
   - Si el producto es `separadores-de-dedos-en-silicona-medica` muestra **TALLA ÚNICA**; los demás productos (Barefoot) siguen mostrando la guía de tallas normal.

## Cambios a nivel de tienda (afectan a TODOS los temas, incluido el publicado)

- **Menú principal** (`main-menu`): se agregó **Blogs** → `/blogs/news` al final (después de "Quienes somos").
- **Blog** `gid://shopify/Blog/124274704753`: título renombrado de "Artículos" a **Blogs**. El handle sigue siendo `news` (URL `/blogs/news`).

## Videos generados en Higgsfield (separadores)

Imagen de referencia del producto importada: media_id `1046fb41-7b12-4930-9751-94c1532c6349`.
Configuración usada: modelo `seedance_2_0`, modo `std`, 9:16, 6 s, 720p, sin audio → **27 créditos** c/u.
(Referencia de costos: Seedance 2.5 1080p 8 s = 96 créditos; Seedance 2.0 1080p 6 s = 54; Seedance 2.0 fast 720p 6 s = 15.)

1. **Video estilo comercial, fondo blanco minimalista (3 tomas)** — job `35741d26-078d-4085-9e7c-06004b4a7cfc`
   - https://d8j0ntlcm91z4.cloudfront.net/user_3JqUmijI9jZdI5ee58BiqJpQA3N/hf_20260926_164159_35741d26-078d-4085-9e7c-06004b4a7cfc.mp4
2. **Producto flotando, cámara orbitando 360°, sin deformación** — job `c943d00f-626d-4434-95f6-f9d550f96aa0`
   - https://d8j0ntlcm91z4.cloudfront.net/user_3JqUmijI9jZdI5ee58BiqJpQA3N/hf_20260926_164713_c943d00f-626d-4434-95f6-f9d550f96aa0.mp4

### Prompt 1 (comercial 3 tomas)
```
Minimalist premium product commercial. The exact medical-grade silicone toe separators from the reference image, keeping their true shape, color, translucency and proportions. Seamless pure white studio background (#FFFFFF), infinite cyclorama, no props, no text, no logos. Shot 1 (0-2s): the toe separators slowly rotate on an invisible turntable, centered, soft diffused top light, subtle soft contact shadow beneath, glossy silicone highlights. Shot 2 (2-4s): smooth macro dolly-in revealing the soft flexible silicone texture as a finger gently squeezes and releases it, showing elasticity. Shot 3 (4-6s): a clean, well-groomed bare foot on the white background, the separators fitted between the toes, toes aligned and relaxed, slow gentle push-in. Clean high-key lighting, 85mm lens look, shallow depth of field, ultra sharp focus on product, calm elegant slow motion, Apple-style minimalism, wellness and comfort mood. Avoid: clutter, colored backgrounds, distorted toes, extra toes, deformed product, text overlays, watermarks.
```

### Prompt 2 (flotando + órbita)
```
Single continuous shot, minimalist premium product video. The exact medical-grade silicone toe separators from the reference image float perfectly still in mid-air in the exact center of the frame, levitating, with a gentle subtle hover. Seamless pure white studio background (#FFFFFF), infinite white cyclorama, no floor line, no props, no text, no logos. Only a very faint, soft, diffused shadow far below the product on the white floor. The camera performs a smooth, slow, steady 360-degree orbit around the product at eye level, constant speed, revealing every side. The product itself remains completely rigid and unchanged: it does not rotate on its own, does not bend, does not stretch, does not morph; its shape, size, proportions, color, translucency and details stay identical to the reference throughout, only the viewing angle changes. Soft high-key studio lighting, subtle glossy highlights on the silicone, sharp focus on the product, 85mm lens look, clean elegant Apple-style commercial. Avoid: deformation, stretching, warping, melting, morphing, extra parts, duplicated product, flicker, camera shake, hard shadows, colored background, text, watermarks.
```

## Pendientes / ideas para retomar

- [ ] Revisar en **Vista previa** el tema Tinker - Bebas Neue (sobre todo "TALLA ÚNICA" en la página de separadores).
- [ ] Publicar Tinker - Bebas Neue desde el admin de Shopify cuando el equipo lo apruebe.
- [ ] Revisar los 2 videos; si el producto se deforma en el de órbita, regenerar usando la foto como `start_image`/`end_image` (~27 créditos).
- [ ] Opcional: cambiar el handle del blog de `news` a `blogs` (con redirección).
- [ ] Ideas: copys en español para los anuncios, código de descuento para la campaña, versión 1:1 para el feed, upscale del video que guste.
