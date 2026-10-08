# Estado financiero de FProject — línea base

Última actualización: **2026-10-08**. Fuentes: Excel `fproject_ecommerce.xlsx` (enviado por Freddy)
y Shopify en vivo (consultado 2026-10-08). Actualiza este archivo cuando cambie un dato.

## 1. Ventas reales (Shopify, 1 ene – 8 oct 2026)

| Mes | Pedidos | Ventas brutas (sin IVA) | Descuentos | Ventas netas | IVA cobrado | Total cobrado |
|---|---|---|---|---|---|---|
| Jun 2026 | 2 | 67.227 | −3.361 | 63.866 | 12.134 | 76.000 |
| Sep 2026 | 2 | 67.226 | −33.277 | 33.950 | 6.450 | 55.351 (incl. 14.951 envío) |
| Resto | 0 | 0 | 0 | 0 | 0 | 0 |

- Todo lo vendido son **4 separadores**; **0 pares de KIBA** vendidos por Shopify.
- Canales: 2 pedidos borrador (Draft Orders), 1 desde la app de iPhone y 1 en tienda online con
  99% de descuento (parece pedido de prueba).
- Shopify **cobra IVA 19% incluido en el precio** → la tienda está configurada como responsable
  de IVA. Confirmar con Freddy/contador si eso es correcto.
- Confirmado por Freddy (2026-10-08): **solo se vende por Shopify**; las ventas a familia y
  amigos u otros canales también se registran en Shopify (pedido borrador). Shopify = fuente única.
- **La mercancía KIBA no ha llegado**: llegada estimada **15 nov 2026**, ya nacionalizada. Por eso
  no hay ventas de KIBA todavía.

## 2. Costo de importación KIBA (hoja 🚢 Importación)

| Concepto | Valor |
|---|---|
| Pares comprados | 750 |
| FOB unitario | USD 19,58 |
| FOB total | USD 14.685 |
| TRM usada | 3.493 COP/USD |
| FOB en COP | 51.294.705 |
| Logística + aduana + comercializadora ("gran total", sin desglose) | 32.826.723 (= 64% sobre FOB) |
| **Costo total del pedido** | **84.121.428** |
| **Costo aterrizado por par** | **112.162** |

### Desglose de los 32,8 M — preliquidación Globalie S.A.S. COT-3172-2026 (vigencia 21-08-2026)
Globalie es la **importadora** (modelo comercializadora): paga aduana e IVA de importación y le
factura a Freddy. La mercancía (FOB) se paga aparte al proveedor y **no** está en los 32,8 M.
Datos de la preliquidación: TRM 3.185,47 · término FOB · carga general 6,10 CBM, 640 kg ·
mercancía declarada **USD 13.335** · flete USD 488 · seguro USD 106 · CIF USD 13.929 (44.370.412).

| Bloque | COP |
|---|---|
| Arancel 15% sobre CIF | 6.655.562 |
| IVA de importación 19% sobre (CIF + arancel) — lo paga y descuenta Globalie | 9.694.935 |
| Flete + seguro internacional | 1.892.169 |
| Gastos en destino (USD 776) | 2.471.925 |
| Puerto | 2.000.000 |
| Aduana (agencia) | 2.313.448 |
| Transporte urbano | 1.826.000 |
| 4×1000 | 90.400 |
| Comisión Globalie (USD 600) | 1.911.282 |
| **Subtotal costos** | **28.855.721** |
| "Diferencia en IVA" + IVA 19% de la factura de Globalie | 3.971.002 |
| **Total a pagar a Globalie** | **32.826.723** |

Fórmula de Globalie (replicada): total = 1,19 × (0,62 × subtotal + IVA importación). La factura
a Freddy sería base 27.585.482 + IVA 5.241.242. Ese IVA de 5,24 M es **descontable para Freddy
solo si es responsable de IVA** y recibe factura electrónica.

Inconsistencias / preguntas abiertas:
- Mercancía declarada USD 13.335 (17,78/par) vs Excel USD 14.685 (19,58/par): diferencia
  USD 1.350. El valor declarado en aduana debe coincidir con lo realmente pagado al proveedor.
- TRM 3.185,47 (preliquidación) vs 3.493 (Excel). Lo que cuenta es la TRM real de cada pago.
- En el cuadro resumen el 4×1000 es 291.200 y el costo bancario 300.000, pero en el detalle
  van 90.400 y 0: quedan **500.800 COP** que podrían sumarse en la liquidación definitiva.
- El IVA de importación entra en la base sobre la que luego se cobra 19% (IVA sobre IVA):
  pedir a Globalie que explique cómo será la factura.
- Es preliquidación: el total final cambia con la TRM. Sensibilidad del total Globalie:
  TRM −5% ≈ 31,4 M · TRM +5% ≈ 34,2 M · TRM +10% ≈ 35,6 M.

### Costo por par recalculado (2026-10-08)
| Escenario | Mercancía (COP) | Globalie | Total | Por par |
|---|---|---|---|---|
| Excel, sin descontar IVA (actual) | 51.294.705 | 32.826.723 | 84.121.428 | **112.162** |
| Excel, responsable de IVA (descuenta 5,24 M) | 51.294.705 | 27.585.482 | 78.880.187 | **105.174** |
| Preliquidación (USD 13.335 a 3.185), sin descontar | 42.478.242 | 32.826.723 | 75.304.965 | 100.407 |
Pendiente: cuánto se pagó realmente al proveedor (USD, COP, fecha, comisiones bancarias).
- Separadores: el Excel no tiene costo en Importación/Productos; en Costos Fijos aparece
  **18.000 COP/unidad** → usar ese valor hasta confirmar.

## 3. Unit economics (línea base calculada, precio con IVA incluido)

| Concepto | KIBA | Separadores (envío solo) |
|---|---|---|
| PVP con IVA | 480.000 | 40.000 |
| Ingreso neto sin IVA (÷1,19) | 403.361 | 33.613 |
| Costo aterrizado | −112.162 | −18.000 |
| Pasarela 3,9% del PVP | −18.720 | −1.560 |
| Comisión Shopify 2% (plan Basic con pasarela externa)* | −9.600 | −800 |
| Envío asumido por la marca | −2.500 | −2.500 |
| Preparación (fulfillment) | −2.300 | −2.300 |
| Devoluciones 2% del neto | −8.067 | −672 |
| **Contribución antes de pauta** | **250.012 (62% del neto)** | **7.781 (23%)** |
| Pauta 25% del PVP (supuesto hoja Productos) | −120.000 | — |
| **Contribución después de pauta** | **130.012 (32%)** | — |

\* El Excel usa 1% (hoja Productos) y 4,29% pasarela+Shopify (hoja Costos Fijos). Con plan
Basic y pasarela externa (Wompi/PayU/MercadoPago) Shopify cobra 2%: verificar en
Configuración → Pagos y en la factura de Shopify.

- ROAS mínimo de equilibrio KIBA ≈ 480.000 ÷ 250.012 ≈ **1,9x**.
- Separadores enviados solos casi no dejan margen: funcionan como **complemento** del pedido
  de KIBA (comparten envío y preparación → contribución ≈ 12.600 sin IVA).

## 4. Costos fijos mensuales (hoja 💰 Costos Fijos)

| Concepto | COP/mes |
|---|---|
| Arriendo / bodega | 840.000 |
| Plataformas (USD 130 × TRM) | ≈ 419.712 |
| Publicidad fija (pauta mínima) | 1.500.000 |
| Nómina, servicios, internet, contador, empaque | 0 (no registrados) |
| **Total** | **≈ 2.759.712** |

- No hay sueldo para Freddy ni contador: el punto de equilibrio real es más alto.
- Punto de equilibrio KIBA (fijos ÷ contribución antes de pauta, pauta tratada como fija):
  2.759.712 ÷ 250.012 ≈ **11 pares/mes**. Con pauta adicional del 25% por venta: ≈ 21 pares/mes.

## 5. Inventario (Shopify, 2026-10-08, ubicación "envia ff bogota")

⚠️ Estas unidades están cargadas como **disponibles** en Shopify, pero físicamente siguen en
importación hasta el ~15 nov. El producto está activo: si alguien compra hoy, sería una preventa
sin aviso. Decidir con Freddy: poner inventario en 0 hasta la llegada o anunciar preventa con
fecha de entrega.

KIBA por color (Green = Yellow = Black):

| Talla | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 |
|---|---|---|---|---|---|---|---|---|---|---|
| Unidades por color | 15 | 30 | 38 | 42 | 42 | 38 | 25 | 15 | 5 | 4 |

- Total KIBA: **762 pares** (Shopify) vs 750 (Excel; difiere en tallas 38, 41 y 45).
- Valor a costo: 762 × 112.162 ≈ **85,5 M COP**; a precio de venta ≈ 365,8 M COP con IVA.
- Separadores: 299 unidades (Excel) → ≈ 5,4 M COP a costo.
- Con 0 ventas reales de KIBA, la prioridad financiera es **rotar el inventario**: es casi todo
  el capital del negocio.

## 6. Mapa del Excel y errores conocidos

Hojas: 📦 Productos · 🏎️ Inventario · 🚢 Importación · 💰 Costos Fijos · ✅ Tareas ·
📊 Dashboard · 📅 Historial Mensual.

Errores / inconsistencias detectados (2026-10-08):
1. **Costos Fijos fila 8**: dice "SEPARADORES DE DEDOS" pero tiene 50 unidades × 480.000 (precio
   de KIBA); la fila 7 de KIBA está en 0. Los 24 M de "ingresos de junio" son un escenario.
2. **Columna D de Costos Fijos** (D22, D34…) quedó en 0 y el **Dashboard lee la columna D** →
   muestra margen 100% y costos 0. Los cálculos válidos están en la columna B.
3. **IVA en 0%** en la hoja Productos, pero Shopify cobra 19% incluido → márgenes sobrestimados
   (el ingreso real por par es 403.361, no 480.000).
4. **Comisiones inconsistentes**: Productos 3,9% + 1%; Costos Fijos 4,29% total. Unificar.
5. **Pauta con dos supuestos**: 25% del PVP por unidad (Productos) vs 1,5 M fijos (Costos Fijos).
6. **Separadores sin costo** en Productos e Importación → margen 100% falso.
7. Costos Fijos B22 suma la pasarela de separadores (800) al costo unitario de KIBA.
8. Inventario: días de inventario con #DIV/0! cuando no hay ventas; "ventas últimos 30 días"
   (17 KIBA, 20 separadores) no coincide con Shopify.
9. Historial Mensual vacío; Dashboard "margen por producto" sin llenar.
10. Plataformas usa `GOOGLEFINANCE` (solo funciona en Google Sheets; en Excel queda el valor fijo).

## 7. Situación tributaria y contable (Freddy, 2026-10-08)
- Factura como **persona natural**.
- La **contabilidad la lleva el skill `contador`** (libros en `contabilidad/`). El contador
  público externo solo hace la **declaración de renta** y las presentaciones que se le envíen,
  y **cobra por presentación**. Correo del contador: _pendiente_. Tarifa por presentación:
  _pendiente_ (presupuestar en el mes de cada vencimiento).
- Por confirmar con el contador: responsabilidad de IVA en el RUT (Shopify ya cobra IVA),
  facturación electrónica, quién figura como importador (Freddy o la comercializadora) y si
  conviene régimen SIMPLE o pasar a SAS. Ojo: vender los 750 pares a precio lleno ≈ 302 M de
  ingresos sin IVA, por encima del tope de 3.500 UVT (≈ 183 M) para no ser responsable de IVA.

## 8. Datos que faltan (preguntar a Freddy cuando sean relevantes)
- Desglose de los 32,8 M de importación (Freddy lo va a enviar); tiempo de reposición desde China.
- Pasarela real usada y su tarifa; días en que la pasarela consigna.
- Saldo de caja actual, deudas o crédito usado para la importación.
- Gasto real en pauta por mes y resultados.
