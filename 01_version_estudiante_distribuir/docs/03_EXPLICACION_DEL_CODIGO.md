# Explicación del código del proyecto

Este proyecto está dividido en varios archivos para que sea más fácil de entender. En proyectos reales, no siempre se escribe todo en un solo archivo. Dividir el código ayuda a organizar responsabilidades.

---

## 1. `src/main.py`

Es el punto de entrada del programa. Coordina todo el proceso:

```text
Leer argumentos -> cargar datos -> validar -> analizar -> generar salidas -> mostrar resumen
```

No debería contener toda la lógica detallada, sino llamar a otros módulos.

---

## 2. `src/finca_auto/lector_csv.py`

Se encarga de leer archivos CSV. Su responsabilidad es abrir el archivo y convertir cada fila en un registro que Python pueda procesar.

Conceptos relacionados:

- Archivo.
- Ruta.
- CSV.
- Fila.
- Columna.

---

## 3. `src/finca_auto/validador.py`

Se encarga de revisar los datos antes de analizarlos.

Ejemplos de validaciones:

- La fecha no debe estar vacía.
- Los valores numéricos no deben ser negativos.
- El responsable no debe estar vacío.
- Las columnas obligatorias deben existir.

---

## 4. `src/finca_auto/analizador.py`

Realiza los cálculos principales:

- Totales.
- Promedios.
- Máximos.
- Mínimos.
- Alertas.
- Tendencias simples.

Este módulo transforma datos en indicadores.

---

## 5. `src/finca_auto/reportes.py`

Genera archivos de salida en formato TXT y JSON.

El TXT sirve para lectura humana. El JSON sirve para guardar datos estructurados que podrían ser usados por otro programa.

---

## 6. `src/finca_auto/backup.py`

Crea una copia del archivo original dentro de `outputs/respaldos`.

La copia incluye fecha y hora para evitar reemplazar respaldos anteriores.

---

## 7. `src/finca_auto/dashboard.py`

Genera una página HTML para visualizar los resultados. Usa HTML, CSS y JavaScript básico. El objetivo es mostrar que un script también puede producir una salida visual.

---

## 8. `src/finca_auto/logger.py`

Crea un registro técnico de ejecución. El log ayuda a saber qué ocurrió durante el proceso.

---

## 9. Por qué se usa esta arquitectura

Esta estructura permite entender mejor el proyecto:

```text
Cada archivo tiene una responsabilidad.
El código es más fácil de leer.
Los errores son más fáciles de ubicar.
Las mejoras se pueden hacer sin dañar todo el sistema.
```
