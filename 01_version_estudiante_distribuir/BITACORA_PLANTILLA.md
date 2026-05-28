# Bitácora técnica - Semana 12
## Scripts, respaldos y reportes

## 1. Datos generales

- nombre: [alejandro velasquez machado]
- Grupo: [completar]
- Fecha: [28/05/2026]
- Modalidad: Individual / Pareja [grupo]
- Nombre del compañero, si aplica: [no aplica / completar]

---

## 2. Objetivo de la práctica

Escribe con tus propias palabras cuál fue el objetivo de esta actividad.

Respuesta:

Aprender a usar un script de Python para automatizar el análisis de datos de una finca, validar información, generar reportes, crear respaldos y mostrar resultados en un dashboard.

---

## 3. Contexto del problema

Explica brevemente cuál era el problema de la finca y por qué se necesitaba automatizar el proceso.

Respuesta:

La finca registraba datos diarios de producción y necesitaba organizar esa información sin hacerlo manualmente. Automatizar el proceso ayuda a evitar errores, ahorrar tiempo y conservar evidencia de los resultados.

---

## 4. Exploración del proyecto

### 4.1 Carpetas identificadas

Escribe qué función cumple cada carpeta.

| Carpeta | Función |
|---|---|
| data | Contiene los archivos CSV de entrada con los datos de producción. |
| src | Contiene el código Python que ejecuta el proceso principal. |
| docs | Contiene documentación de apoyo y guías de lectura. |
| outputs/reportes | Guarda los reportes TXT y JSON generados automáticamente. |
| outputs/respaldos | Guarda copias de seguridad del archivo analizado. |
| outputs/logs | Guarda los registros técnicos de ejecución. |
| outputs/dashboard | Guarda el archivo HTML del panel visual. |

### 4.2 Captura del proyecto abierto en VS Code

Pega aquí la captura o indica el nombre del archivo de evidencia.

[pendiente por capturar]

---

## 5. Ejecución del diagnóstico

Comando utilizado:

```bash
python src/diagnostico_entorno.py
```

Resultado observado:

El diagnóstico confirmó que Python funciona correctamente, que las carpetas principales existen y que el archivo base `data/produccion_finca.csv` está disponible.

Captura:

[pendiente por capturar]

---

## 6. Ejecución del script principal

Comando utilizado:

```bash
python src/main.py
```

Mensajes observados en la terminal:

El programa se ejecutó correctamente, validó los datos sin errores, generó los archivos de salida y mostró un resumen con totales, promedios, alertas y tendencia.

Archivos generados:

| Archivo | Ubicación | Para qué sirve |
|---|---|---|
| Reporte TXT | `outputs/reportes/` | Resume los resultados en texto. |
| Resumen JSON | `outputs/reportes/` | Guarda los resultados en formato estructurado. |
| Respaldo CSV | `outputs/respaldos/` | Conserva una copia del archivo original. |
| Dashboard HTML | `outputs/dashboard/` | Presenta los resultados de forma visual. |
| Log | `outputs/logs/` | Registra la ejecución técnica del programa. |

Captura de la terminal:

[pendiente por capturar]

---

## 7. Análisis del reporte

Nombre del reporte generado:

`reporte_semanal_2026-05-28_07-24-29_769093.txt`

Ubicación:

`outputs/reportes/`

Responde:

1. ¿Cuál fue el total semanal de leche?
   169.5 litros.
2. ¿Cuál fue el promedio diario de leche?
   24.21 litros.
3. ¿Qué día tuvo mayor producción?
   Jueves, con 27.5 litros.
4. ¿Qué día tuvo menor producción?
   Domingo, con 21.0 litros.
5. ¿Qué alertas aparecieron?
   Apareció una alerta de leche baja el 2026-05-24 (Domingo).
6. ¿Qué decisión podría tomar la finca con ese reporte?
   Revisar por qué bajó la producción ese día y reforzar alimentación, manejo o condiciones del sistema de producción.

Captura del reporte:

[pendiente por capturar]

---

## 8. Análisis del respaldo

Nombre del respaldo generado:

`respaldo_produccion_finca_2026-05-28_07-24-29_775813.csv`

Ubicación:

`outputs/respaldos/`

Responde:

1. ¿Qué archivo fue respaldado?
   El archivo `data/produccion_finca.csv`.
2. ¿Por qué el respaldo incluye fecha y hora?
   Para identificar cuándo se creó y evitar sobrescribir respaldos anteriores.
3. ¿Qué riesgo se reduce al crear respaldos?
   Se reduce el riesgo de perder información por errores, borrados accidentales o daño del archivo original.

Captura del respaldo:

[pendiente por capturar]

---

## 9. Dashboard visual

Archivo abierto:

```text
outputs/dashboard/index.html
```

Responde:

1. ¿Qué información se entiende mejor en el dashboard?
   Los indicadores principales, las alertas y la comparación visual de la producción diaria.
2. ¿Qué ventaja tiene presentar resultados visualmente?
   Permite interpretar los resultados más rápido y de forma más clara que solo con texto.
3. ¿Qué mejorarías del dashboard?
   Agregaría más gráficas y una diferenciación visual más marcada para valores altos, bajos y normales.

Captura del dashboard:

[pendiente por capturar]

---

## 10. Caso con errores

Comando utilizado:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

Errores o advertencias observadas:

| Fila | Problema encontrado | Por qué afecta el resultado |
|---|---|---|
| 3 | `leche_litros` negativo | No representa una producción real. |
| 4 | `fecha` con formato inválido | Dificulta el análisis por fecha. |
| 5 | `leche_litros` no numérico | No se puede sumar ni promediar. |
| 6 | `alimento_kg` vacío | Falta un dato necesario para calcular resultados. |
| 7 | `responsable` vacío | No permite identificar quién registró la información. |

Conclusión del análisis de errores:

El programa detectó los datos incorrectos y continuó con los registros válidos. Esto demuestra que validar información antes de procesarla es fundamental para evitar resultados engañosos.

---

## 11. Modificación de datos

Dato modificado:

[pendiente por completar]

Antes:

[pendiente por completar]

Después:

[pendiente por completar]

¿Qué cambió en el reporte?

[pendiente por completar]

¿Por qué cambió?

[pendiente por completar]

---

## 12. Reto de mejora

Describe la mejora que propusiste:

Se mejoró el sistema para que los archivos de salida usen marcas de tiempo con microsegundos, evitando que se sobrescriban cuando hay varias ejecuciones en el mismo segundo.

Explica por qué sería útil:

Es útil porque conserva cada ejecución como evidencia separada y evita perder reportes, respaldos o logs recientes.

Indica qué archivo modificaste o qué idea planteaste:

Se modificaron `src/finca_auto/reportes.py`, `src/finca_auto/backup.py` y `src/finca_auto/logger.py`.

---

## 13. Conclusión personal

Escribe una conclusión de mínimo 8 líneas donde expliques qué aprendiste sobre:

- Scripts.
- Automatización.
- Respaldos.
- Reportes.
- Validación de datos.
- Uso de VS Code.
- Aplicación en la vida real.

Conclusión:

Aprendí que un script permite automatizar tareas repetitivas de manera más rápida y ordenada.
También comprendí que la automatización reduce errores y mejora el control de la información.
Los respaldos son importantes porque protegen los datos originales si ocurre un problema.
Los reportes sirven para resumir resultados y apoyar la toma de decisiones.
La validación de datos evita que un error en la entrada afecte todo el análisis.
Trabajar en VS Code facilita ejecutar, revisar y organizar el proyecto en un solo entorno.
Esta práctica se puede aplicar en una finca, una tienda o un colegio para manejar información real.
En general, entendí mejor la relación entre entrada, proceso y salida dentro de un programa.
