# Ejercicio 4 - Modificar datos y comparar resultados

## Objetivo

Observar cómo los cambios en los datos de entrada afectan los resultados.

## Instrucciones

1. Abre `data/produccion_finca.csv`.
2. Cambia un valor de `leche_litros`.
3. Guarda el archivo.
4. Ejecuta:

```bash
python src/main.py
```

5. Compara el nuevo reporte con el anterior.

## Preguntas

1. ¿Qué dato modificaste?
   **Respuesta:** Modifiqué el valor de `leche_litros` del primer día de la semana (lunes).

2. ¿Cuál era el valor anterior?
   **Respuesta:** El valor anterior era 23.5 litros.

3. ¿Cuál fue el nuevo valor?
   **Respuesta:** Lo cambié a 35.0 litros (aumenté la producción del lunes).

4. ¿Qué cambió en el reporte?
   **Respuesta:** El total semanal aumentó de 169.5 a 181.0 litros. El promedio diario pasó de 24.21 a 25.86 litros. El nuevo reporte mostró el lunes como el día de mayor producción con 35.0 litros en lugar del jueves.

5. ¿Por qué cambió?
   **Respuesta:** Porque los cálculos de suma y promedio incluyen el nuevo valor. Si cambias un dato de entrada, todos los cálculos que dependen de él se recalculan automáticamente. El programa relee el archivo modificado y genera nuevos resultados.

6. ¿Qué demuestra esto sobre entrada y salida?
   **Respuesta:** Demuestra el modelo Entrada → Proceso → Salida. La entrada (datos en CSV) directamente afecta la salida (reporte). Si cambias la entrada, la salida cambia automáticamente. Esto prueba que:
   - Los datos de entrada son el origen de todo.
   - El programa depende completamente de la calidad de la entrada.
   - Cambios pequeños en entrada generan cambios en la salida.
   - Por eso validar entrada es tan importante.
