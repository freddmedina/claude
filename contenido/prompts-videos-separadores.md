# Prompts para Higgsfield — videos de los separadores F Movement

Estos prompts recrean los 2 videos con la estética de marca: separador negro sobre verde lima neón o sobre el degradado rosa-naranja de Instagram.
Los prompts van en **inglés** porque los modelos de video responden mejor así. Abajo de cada uno está lo que hace, en español.

## Configuración recomendada

| Ajuste | Valor |
|---|---|
| Modelo | **Seedance 2.0 · modo fast** (el más barato para probar) o Seedance 2.5 si quieres más calidad |
| Formato | **9:16** (Reels) |
| Duración | 6 segundos |
| Resolución | 720p |
| Audio | Desactivado (el audio se pone en Instagram con un sonido en tendencia) |
| Referencia | **Sube una foto real del separador** como *image reference* para que el modelo copie la forma exacta |

**Costo en tus créditos (consultado el 27/09/2026):**
- Seedance 2.0 fast: **15 créditos** por video.
- Seedance 2.5: **42 créditos** por video.

Con los 56 créditos que tienes te alcanza para **3 videos en 2.0 fast**, o para 1 en 2.5.
Prueba primero en 2.0 fast, y usa 2.5 solo para la versión final si la necesitas.

> Los videos que ya tienes (`contenido/videos-separadores/`) sirven para publicar tal cual. Estos prompts son para hacer versiones nuevas nativas, con luz y sombras hechas sobre el color, o para generar más clips en el lanzamiento.

---

## PROMPT 1 — "Manos + pies" (flexibilidad y uso)

```
Vertical 9:16 product video, clean studio shot on a seamless solid neon lime green
background (#B8F03C), soft diffused light, subtle natural shadows on the floor.
A black medical-grade silicone toe separator (five soft loops, wavy top edge, matte
texture, small embossed "F" logo) rests on the lime floor. A hand enters the frame and
presses and bends the separator with two fingers to show how soft and flexible it is,
then releases it and it springs back to shape. Cut to a close-up of two bare feet
standing on the same lime background, each foot wearing a black toe separator, toes
naturally spread apart and relaxed. Smooth slow camera push-in, premium minimalist
e-commerce look, realistic skin texture, sharp focus on the product, no text, no logos
other than the product's, no extra objects.
```

**Qué hace:** repite la idea del video "manos". Se ve el separador sobre el lima, una mano lo dobla para mostrar lo flexible que es, y luego aparecen los pies con los separadores puestos y los dedos abiertos.
**Úsalo para:** el Reel "Tus dedos no nacieron pegados" (1 de octubre).

---

## PROMPT 2 — "Giro flotante" (producto hero)

```
Vertical 9:16 hero product video. A single black medical-grade silicone toe separator
(wavy top edge with five toe loops, matte soft-touch texture, small embossed "F" logo)
floats in mid-air and slowly rotates 360 degrees in the center of the frame. Background
is a smooth vertical gradient from hot pink magenta (#F45BC6) at the top to warm orange
(#FF9A4A) at the bottom. Soft studio lighting with a gentle rim light that outlines the
product edges, a soft blurred shadow on the floor below it that follows the rotation.
Seamless loop, calm and premium, minimalist sportswear advertising style, sharp focus,
no text, no hands, no extra objects.
```

**Qué hace:** el separador flota y gira 360° sobre el degradado rosa-naranja, con una luz que marca el borde y la sombra en el piso, en loop.
**Variante lima:** cambia la línea del fondo por
`Background is a seamless solid neon lime green (#B8F03C).`
**Úsalo para:** el Reel "El accesorio que tu fisio sí usa" (8 de octubre), en historias de lanzamiento o como portada de la destacada "Separadores".

---

## Consejos

- Si la forma del separador sale mal, sube 2 fotos de referencia: una de frente y una de lado.
- Si el fondo sale "sucio" o con objetos, agrega al final: `plain empty background, nothing else in the scene`.
- Los modelos no escriben bien texto en español. Pon los textos encima del video en Instagram o en CapCut, no en el prompt.

---

## PROMPT DEL REEL 1 OCT — "Manos + pies" en fondo lima (versión final recomendada)

Basado en el prompt original que generó el video "manos" (ver `CONTEXTO.md` en la rama
`claude/sleepy-ritchie-ptcpxp`), con el fondo cambiado al lima de Instagram y el producto descrito
como es en realidad (negro mate, no translúcido).

- Modelo: **Seedance 2.0 · std** · 9:16 · 6 s · 720p · sin audio → ~27 créditos
  (o Seedance 2.0 fast → 15 créditos).
- Referencia: imagen del separador `media_id 1046fb41-7b12-4930-9751-94c1532c6349` como *image reference*.

```
Minimalist premium product commercial, vertical 9:16. The exact black medical-grade silicone toe separators from the reference image, keeping their true shape, matte black color, wavy top edge, five toe loops and proportions. Seamless solid neon lime green studio background (#B8F03C), infinite cyclorama, no props, no text, no logos other than the product's. Shot 1 (0-2s): the pair of toe separators rests on the lime floor, slow push-in, soft diffused top light, subtle soft contact shadow beneath. Shot 2 (2-4s): smooth macro shot, two fingers press and bend the separator to show how soft and flexible the silicone is, then release and it springs back to shape. Shot 3 (4-6s): two clean, well-groomed bare feet standing on the lime background, each wearing a black toe separator, toes naturally spread and relaxed, slow gentle push-in. Clean bright studio lighting, 85mm lens look, shallow depth of field, ultra sharp focus on the product, calm elegant slow motion, energetic sportswear-brand aesthetic. Avoid: clutter, white or gray background, distorted toes, extra toes, deformed product, translucent product, text overlays, watermarks.
```
