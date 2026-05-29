# Ejercicio 3 - Analizar errores

## Objetivo

Comprender la importancia de validar datos antes de generar reportes.

## Comando

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

## Preguntas

1. ¿Qué errores o advertencias se detectaron?
   **Respuesta:** El programa detectó 5 problemas: producción de leche negativa, fecha con formato inválido, valor no numérico en un campo de cantidad, campo vacío en alimento, y responsable sin asignar.

2. ¿Qué fila tuvo problemas?
   **Respuesta:** Múltiples filas tuvieron problemas: la fila 3 tenía leche negativa, la fila 4 tenía fecha mal formateada, la fila 5 tenía un valor no numérico, la fila 6 tenía un campo vacío, y la fila 7 no tenía responsable asignado.

3. ¿Qué campo estaba incorrecto?
   **Respuesta:** Varios campos estaban incorrectos: `leche_litros` (valor negativo), `fecha` (formato erróneo), columna numérica (valor de texto), `alimento_kg` (vacío), y `responsable` (sin valor).

4. ¿El programa continuó o se detuvo?
   **Respuesta:** El programa continuó ejecutándose pero mostró advertencias claras de los errores detectados. No generó resultados confiables porque los datos estaban comprometidos.

5. ¿Por qué no se deben ignorar los datos incorrectos?
   **Respuesta:** Porque los datos incorrectos generan reportes falsos que llevan a decisiones equivocadas. Un error en los datos de entrada produce errores en la salida (reportes), y esto puede causar pérdidas económicas reales en la finca.

## Análisis

Explica cómo un dato incorrecto podría afectar una decisión real en una finca.

**Respuesta:**

Imagina que el archivo registra leche negativa por error de digitación. El programa calcula un promedio que incluye ese valor negativo, resultando en un promedio muy bajo que no es real. El encargado de la finca ve ese reporte y piensa que la producción está en crisis, cuando en realidad los datos están dañados.

Como consecuencia, toma decisiones innecesarias:
- Vende una vaca que en realidad está sana.
- Gasta dinero en veterinario cuando no es necesario.
- Cambia la alimentación de los animales.
- Pierde dinero por decisiones basadas en información falsa.

Por eso la validación de datos es crítica: evita que datos dañados produzcan decisiones costosas. El programa detecta estos errores antes de que causen daño.
