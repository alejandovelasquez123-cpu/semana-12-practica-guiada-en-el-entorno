# Respaldos y reportes

## 1. Qué es un respaldo

Un respaldo es una copia de seguridad de información importante. En esta práctica, el respaldo conserva una copia del archivo CSV usado por el programa.

## 2. Por qué no se debe reemplazar siempre el mismo respaldo

Si todos los respaldos tienen el mismo nombre, el respaldo nuevo reemplaza al anterior. Eso puede ser peligroso porque se pierde el historial.

Por eso el proyecto usa nombres con fecha y hora.

Ejemplo:

```text
respaldo_produccion_finca_2026-05-27_154500.csv
```

## 3. Qué es un reporte

Un reporte es un documento que resume resultados. En lugar de leer todas las filas del CSV, el reporte muestra indicadores importantes.

## 4. Diferencia entre respaldo y reporte

| Elemento | Función |
|---|---|
| Respaldo | Proteger una copia de los datos originales. |
| Reporte | Presentar resultados calculados a partir de los datos. |

## 5. Qué debe tener un buen reporte

Un buen reporte debe incluir:

- Fecha de generación.
- Archivo analizado.
- Total de registros válidos.
- Registros con errores.
- Totales.
- Promedios.
- Alertas.
- Observaciones.

## 6. Pregunta de análisis

¿Qué sería más grave: perder el reporte o perder el archivo de datos original? Explica tu respuesta en la bitácora.
