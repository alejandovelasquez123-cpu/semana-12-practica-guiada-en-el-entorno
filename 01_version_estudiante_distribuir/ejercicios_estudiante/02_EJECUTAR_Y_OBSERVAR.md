# Ejercicio 2 - Ejecutar y observar

## Objetivo

Ejecutar el script principal y observar las salidas generadas.

## Comandos

```bash
python src/diagnostico_entorno.py
```

```bash
python src/main.py
```

## Preguntas

1. ¿Qué mensaje mostró el diagnóstico?
   **Respuesta:** El diagnóstico confirmó que Python funciona correctamente, que todas las carpetas principales existen y que el archivo `data/produccion_finca.csv` está disponible para procesarse.

2. ¿Qué mensaje mostró el script principal al terminar?
   **Respuesta:** Mostró un bloque de resumen rápido con los totales (169.5 litros de leche, por ejemplo), promedios diarios, día de mayor y menor producción, alertas detectadas y la ruta del dashboard generado.

3. ¿Qué archivos nuevos se generaron?
   **Respuesta:** Se generaron 5 tipos de archivos: un reporte TXT, un resumen JSON, un respaldo CSV, un archivo de log, y el dashboard HTML en la carpeta `outputs/`.

4. ¿Dónde se guardó el reporte?
   **Respuesta:** En `outputs/reportes/reporte_semanal_FECHA_HORA.txt`. Contiene totales, promedios, alertas y observaciones técnicas.

5. ¿Dónde se guardó el respaldo?
   **Respuesta:** En `outputs/respaldos/respaldo_produccion_finca_FECHA_HORA.csv`. Es una copia exacta del archivo original con fecha y hora para identificar cuándo se creó.

6. ¿Qué información aparece en el dashboard?
   **Respuesta:** Indicadores principales (totales y promedios), día de mayor y menor producción, alertas de producción baja, y un gráfico o tabla visual con la producción diaria.

## Evidencia

Toma capturas de:

- Terminal: `evidencias/evidencia_05_ejecucion_exitosa.png`
- Reporte generado: `evidencias/evidencia_06_dashboard_visual.png` (contiene el resumen del reporte)
- Respaldo generado: `evidencias/evidencia_07_archivos_reportes_generados.png`
- Dashboard: `evidencias/evidencia_06_dashboard_visual.png`
