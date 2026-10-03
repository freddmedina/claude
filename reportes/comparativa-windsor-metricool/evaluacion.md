# Evaluación: Windsor.ai vs Metricool (Instagram @fproject_at, 06/07–03/10/2026)

**Veredicto:** hoy el reporte **más completo es el de Windsor (39/50 frente a 28/50)**: tiene los 90 días, las 10 publicaciones y los datos del perfil.
Aun así, si vas a quedarte con **una sola**, te recomiendo **Metricool**. Casi todo lo que le falta es temporal, porque se conectó hoy, y lo que le falta a Windsor (mejores horas, hashtags y calendario) es permanente. Además, Windsor está en plan Trial.
Antes de que caduque el Trial, guarda el histórico de Windsor (`windsor_diario.csv` ya lo tiene).

## Puntuación (0–5)

`*` = limitación **temporal** de Metricool (debería mejorar a medida que sincronice). Sin marca = limitación **permanente** o de la plataforma.

| Criterio | Windsor | Metricool | Comentario |
|---|---|---|---|
| Cobertura histórica de los 90 días | 5 | 2 | W: 90/90 días. M: alcance en 62/90 (desde el 02/08). Lo anterior al 02/08 no lo trajo, y parece que no lo traerá. |
| Métricas de cuenta diarias | 5 | 2* | W: vistas, alcance, interacciones desglosadas y reparto entre seguidores y no seguidores. M: vistas solo de 7 días y seguidores solo de 5. |
| Cobertura de publicaciones | 5 | 3 | W: 10/10. A M le faltan las 3 publicaciones de julio, que quedan fuera de su histórico. |
| Profundidad por publicación | 4 | 3 | W: visitas al perfil, seguidores ganados por post, salto en los 3 primeros segundos y texto de comentarios. M: desglose de me gusta y comentarios, más engagement %. |
| Audiencia / demografía | 4 | 4 | Iguales en contenido. W da números absolutos; M da país y ciudad en %. |
| Historias | 1 | 1* | Ninguna trae datos (0 registros). Instagram solo expone 24 h de historias. |
| Extras accionables (horas, hashtags, programación) | 1 | 5 | Solo M los tiene. En W es una carencia permanente. |
| Datos del perfil (bio, enlace) | 5 | 2 | M no ve la bio ni el enlace, que es justo donde está el problema del Linktree. |
| Exactitud / consistencia | 4 | 3 | Ver errores abajo. Los totales de W cuadran al 100 %, pero dos cifras clave de M no se pueden reproducir. |
| Utilidad para el negocio (integraciones, escritura) | 5 | 3 | W: más de 350 conectores (podría cruzar con Shopify), publicar y moderar comentarios. M: programar publicaciones con flujo de aprobación. |
| **Total** | **39/50** | **28/50** | Si se llenan los huecos marcados con `*`, M podría acercarse a unos 32. |

**Riesgo de costo y continuidad (fuera del total):** Windsor está en **Trial gratis**, así que caduca y para seguir habrá que pagar (el precio no está en los reportes). De Metricool, la API no informa el plan; confírmalo en tu cuenta antes de decidir.

## Verificación con los CSV: lo que cuadra
- **Windsor:** cuadran los 90 días sin huecos ni duplicados, todos los totales (24.433 vistas, 9.765 de alcance, 672 interacciones, 531 me gusta…), las cifras por mes y los picos del 17/08 y del 02/09.
- **Metricool:** cuadran los 62 días con alcance, 7.285 de alcance, 427 cuentas que interactuaron, 3.373 vistas en 7 días, seguidores 8 ganados / 3 perdidos y los picos.
- **Coincidencia entre plataformas:** alcance y cuentas que interactuaron coinciden **exactamente en los 62 días** compartidos, y las vistas en los 7. Las interacciones por post de Metricool también cuadran con su propia fórmula (me gusta + comentarios + guardados + compartidos).

## Errores e inconsistencias encontrados
1. **Ambos: "12 días seguidos sin publicar (14–25/09)".** Según sus propias tablas, entre el post del 28/08 y el del 29/09 no hubo ninguna publicación en el feed: **más de un mes**. Los días 14–25/09 son solo el tramo de actividad mínima.
2. **Windsor: "0 interacciones" del 14 al 25/09.** El 14/09 hubo 1 interacción.
3. **Ambos: el pico es el 17/08, pero la publicación del atleta aparece con fecha 18/08.** Probablemente es un desfase de zona horaria (UTC frente a Bogotá); conviene aclararlo para no atribuir mal los picos.
4. **Windsor: pico del 02/09 sin explicación.** Ese día hubo 2.037 vistas y 107 interacciones sin ninguna publicación en la lista. Lo mismo pasa, en menor escala, el 24/07 y el 13/09. Seguramente fueron historias u otro contenido que ninguna plataforma registró.
5. **Windsor: dato anómalo.** El 24/08 hay `reposts = -1`.
6. **Windsor: el desglose no suma el total.** Me gusta + comentarios + guardados + compartidos + reposts + respuestas da 644, pero las interacciones totales son 672 (diferencia en 14 días). El reparto entre seguidores y no seguidores tampoco suma exacto (9.770 frente a 9.765).
7. **Metricool: "alcance medio por post 619".** Esa cifra sale solo de los 6 posts, **sin el reel**: con las 7 publicaciones de la tabla serían 581. No lo aclara.
8. **Metricool: "engagement agregado 6,49 %".** No se puede reproducir con la tabla: interacciones ÷ alcance da 6,9 % y la media de los porcentajes por post da 7,6 %.
9. **Diferencias menores por la hora de extracción.** El post del 03/10 tiene 308 vistas y 126 de alcance en Windsor, frente a 305 y 120 en Metricool. Es normal y no es un error grave.

Lo que no se puede verificar porque no está en los CSV: los datos por publicación, la audiencia, los 19 seguidores nuevos y los 0 toques en el enlace de Windsor, y los hashtags y las mejores horas de Metricool.

## Recomendación
- **Quédate con Metricool como herramienta del día a día.** Te sirve para decidir *cuándo* publicar (10 a. m. entre semana), para ver qué hashtags funcionan y para programar. Eso es justo lo que te hace falta, porque el problema principal fue pasar un mes sin publicar.
- **Aprovecha Windsor mientras dure el Trial** para tres cosas: guardar el histórico (antes del 02/08 no lo tendrás en ningún otro sitio), revisar los seguidores ganados y las visitas al perfil por post y, si quieres, hacer un cruce puntual con Shopify.
- **Arregla el enlace de la bio** (hoy lleva a linktr.ee/freddmedinaft y tiene 0 toques). Ninguna de las dos herramientas lo resuelve por ti.

**Qué cambiaría la recomendación:**
- Que dentro de 2–4 semanas Metricool **siga sin vistas ni seguidores diarios**: entonces sus huecos no eran temporales.
- Que su plan resulte de pago o muy limitado.
- Que quieras **un solo panel Instagram + Shopify (+ anuncios)** y el precio de Windsor te parezca razonable: entonces Windsor gana.
