# Guía para armar el correo de bienvenida en Shopify Messaging

Copiar y pegar bloque por bloque. Versión HTML completa: `correos/bienvenida-newsletter.html`.

## Dónde
Admin → **Marketing → Automatizaciones** → **Crear automatización** →
**"Dar la bienvenida a nuevos suscriptores"** (en inglés: *Welcome new subscribers*) →
clic en el paso **Enviar correo de marketing** → **Editar correo**.

## Opción rápida (si el editor tiene sección de código)
Si al pulsar **Agregar sección** aparece **"Liquid personalizado"** / **"Custom Liquid"** / **"HTML"**:
borra las secciones de la plantilla, agrega esa sección y pega el contenido de
**`correos/bienvenida-newsletter-shopify.html`** (versión "solo contenido": sin `<html>`, `<head>`,
`<body>`, comentarios ni fuentes externas, con todos los estilos en línea).
⚠️ No pegar `bienvenida-newsletter.html` (documento completo): el editor descarta la cabecera y el
cuerpo y el diseño se pierde (le pasó a Fredd el 2026-09-26).
Luego ve directo a **Probar y activar**.

## Opción por bloques

**Asunto:** Bienvenido a FProject: tus pies te lo van a agradecer 👣

**Texto de vista previa:** Gracias por unirte. Te cuento qué vas a recibir y por dónde empezar.

**Colores del correo** (Configuración del correo / Estilo):
fondo `#f1ede7` · fondo del contenido `#ffffff` · botones `#c3cca6` con texto `#000000`.

1. **Encabezado / Logo:** subir o elegir de Archivos `logo-fproject-oscuro.png`, ancho ~240 px, centrado.

2. **Texto (título)**, fondo `#c3cca6`, centrado:
   > **BIENVENIDO A LA COMUNIDAD FPROJECT**
   > El pie no necesita más tecnología. Necesita libertad.

3. **Texto:**
   > ¡Hola! 👋
   >
   > Soy **Fredd Medina**, fisioterapeuta especializado en pie y movimiento y fundador de FProject. Gracias por dejarnos tu correo, de verdad.
   >
   > En 13 años pasando consulta he visto lo mismo una y otra vez: pies débiles, dedos apretados y molestias que empiezan desde abajo. Por eso nació FProject: para que tus pies vuelvan a trabajar como fueron diseñados, con calzado y herramientas pensadas desde la fisioterapia.

4. **Texto** (fondo `#faf9f1`):
   > **¿QUÉ VAS A RECIBIR?**
   > 🦶 **Contenido para cuidar tus pies**, explicado de forma sencilla y con respaldo en fisioterapia.
   > 🏋️ **Ejercicios y consejos prácticos** para moverte mejor en el día a día y en el gimnasio.
   > 🎁 **Ofertas y lanzamientos** antes que nadie.

5. **Texto:**
   > Si el barefoot es nuevo para ti, tranquilo: en Colombia todavía poca gente lo conoce. Te dejé una guía para empezar:

6. **Botón:** "Leer: ¿Qué es el calzado barefoot?" →
   `https://fprojectcompany.com/blogs/news/que-es-el-calzado-barefoot`

7. **Productos** (sección de producto, o texto + botón):
   - **KIBA Barefoot:** Suela flexible, cero drop y puntera ancha. Incluye **plantilla de transición** para empezar poco a poco. → `https://fprojectcompany.com/products/barefoot`
   - **Separadores de dedos:** Silicona médica, con guía ilustrada de uso y ejercicios. → `https://fprojectcompany.com/products/separadores-de-dedos-en-silicona-medica`

8. **Texto:**
   > **Un consejo de fisio para empezar:** si vienes de zapato convencional, haz la transición poco a poco. Tus pies necesitan tiempo para ganar fuerza, y eso está bien.
   >
   > Por eso nuestros KIBA vienen con una **plantilla de transición**: te da un poco más de soporte mientras tus pies se adaptan. Cuando te sientas listo, la quitas y vives **la experiencia barefoot completa**.
   >
   > ¿Tienes alguna duda? Responde este correo y te leo personalmente.
   >
   > Un abrazo,
   > **Fredd Medina**
   > Fisioterapeuta · Fundador de FProject

9. **Pie de página** (fondo `#000000`, texto blanco): logo `logo-fproject-blanco.png` (~160 px) y
   > El pie no necesita más tecnología. Necesita libertad.
   > fprojectcompany.com
   > El contenido de nuestros correos tiene fines educativos y no reemplaza una valoración profesional.

   (Shopify agrega solo el enlace para darse de baja y la dirección de la tienda.)

## Probar y activar
1. **Guardar** → **Enviar prueba** a tu correo → revisar en el celular.
2. Volver a la automatización → **Activar**.
3. Suscribirse desde la web con otro correo y confirmar que llega.
