# Taller práctico - Actividad 2 Semana 12
## Práctica guiada en el entorno

Responde después de ejecutar el proyecto. No respondas solo con teoría: usa lo que observaste en VS Code, la terminal y los archivos generados.

---

## Parte A. Comprensión del proyecto

1. ¿Cuál es el problema que intenta resolver este proyecto?
   Automatizar el análisis de datos de una finca para evitar trabajo manual, reducir errores y generar evidencia de los resultados.
2. ¿Qué tarea repetitiva se automatiza?
   Leer datos, validarlos, generar reportes, crear respaldos y construir un dashboard.
3. ¿Qué archivo funciona como entrada principal?
   `data/produccion_finca.csv`.
4. ¿Qué carpetas contienen los resultados generados?
   `outputs/reportes`, `outputs/respaldos`, `outputs/logs` y `outputs/dashboard`.
5. ¿Qué diferencia hay entre un reporte y un respaldo?
   El reporte resume y analiza los datos; el respaldo guarda una copia del archivo original para proteger la información.
6. ¿Por qué el proyecto genera también un dashboard?
   Para mostrar los resultados de manera visual y facilitar su interpretación.
7. ¿Qué papel cumple el archivo JSON generado?
   Guarda un resumen estructurado de los resultados para que pueda usarse en otros procesos o sistemas.
8. ¿Por qué es importante guardar logs?
   Porque permiten revisar qué pasó durante la ejecución y ayudan a depurar errores o confirmar que el proceso terminó bien.

---

## Parte B. Análisis de ejecución

9. Escribe el comando que usaste para ejecutar el diagnóstico.
   `python src/diagnostico_entorno.py`
10. Escribe el comando que usaste para ejecutar el proyecto principal.
   `python src/main.py`
11. ¿Qué mensaje de la terminal te indicó que el proceso terminó correctamente?
   El bloque final que muestra `Resultados generados`, el resumen rápido y la ruta del dashboard.
12. ¿Qué archivos nuevos aparecieron después de ejecutar el programa?
   Un reporte TXT, un resumen JSON, un respaldo CSV, un log y el dashboard HTML.
13. ¿Qué información contenía el reporte TXT?
   Totales, promedios, día de mayor y menor producción, alertas y una observación técnica.
14. ¿Qué información se veía mejor en el dashboard?
   Los indicadores principales, las alertas y la comparación visual de la producción diaria.
15. ¿Qué evidencia demuestra que el respaldo se creó?
   La aparición de un archivo `respaldo_*.csv` dentro de `outputs/respaldos`.

---

## Parte C. Validación y errores

16. Ejecuta el proyecto con el archivo `produccion_finca_con_errores.csv`. ¿Qué problemas detectó el programa?
   Detectó producción negativa, fecha con formato inválido, un valor no numérico, un campo vacío y un responsable vacío.
17. ¿Qué puede pasar si un programa calcula resultados usando datos incorrectos?
   Puede producir reportes falsos, tomar malas decisiones y ocultar problemas reales.
18. ¿Por qué un valor negativo en producción de leche no tiene sentido?
   Porque la producción es una cantidad física y no puede ser menor que cero.
19. ¿Por qué una fecha mal escrita puede afectar el análisis?
   Porque dificulta ordenar los registros, compararlos por día y detectar tendencias.
20. ¿Qué diferencia hay entre un error que detiene el programa y una advertencia?
   El error impide continuar con normalidad; la advertencia informa un problema que puede seguir permitido dependiendo de la lógica del programa.

---

## Parte D. Relación con contexto real

21. ¿Cómo podría usarse este sistema en una tienda?
   Para controlar ventas, inventario, productos con bajo stock y generar reportes diarios o semanales.
22. ¿Cómo podría usarse en una institución educativa?
   Para registrar notas, asistencia, entregas y emitir reportes de seguimiento.
23. ¿Cómo podría usarse en una finca diferente?
   Para controlar leche, cultivos, alimento, clima y productividad por periodo.
24. ¿Qué datos cambiarías si el sistema fuera para controlar inventario de una tienda?
   Cambiaría leche, maíz y lluvia por producto, cantidad, precio, proveedor y fecha de entrada o salida.
25. ¿Qué reporte automático sería útil para un colegio?
   Un reporte de asistencia y rendimiento académico por curso o por estudiante.

---

## Parte E. Pensamiento técnico

26. Explica el flujo `entrada -> proceso -> salida` usando este proyecto.
   La entrada es el CSV, el proceso es leer, validar y analizar los datos, y la salida son los reportes, el respaldo, el dashboard y el log.
27. ¿Qué ventaja tiene dividir el código en varios archivos dentro de `src/finca_auto`?
   Hace el proyecto más ordenado, fácil de mantener y más simple de revisar o corregir por partes.
28. ¿Por qué es mejor guardar reportes con fecha y hora?
   Porque permite identificar cada ejecución y evita que un archivo nuevo reemplace uno anterior.
29. ¿Qué pasaría si todos los respaldos tuvieran el mismo nombre?
   Se sobrescribirían entre sí y se perderían copias anteriores.
30. ¿Qué mejora técnica propondrías al proyecto?
   Agregar más gráficas al dashboard o crear alertas adicionales cuando la producción caiga demasiado.

---

## Parte F. Conclusión

31. Escribe una conclusión de mínimo 8 líneas explicando qué aprendiste y cómo aplicarías este conocimiento en otro contexto.

Aprendí que un script permite automatizar tareas repetitivas de forma rápida y consistente.
También entendí que validar datos es necesario para evitar resultados incorrectos.
Los respaldos protegen la información y ayudan a recuperar archivos si ocurre un problema.
Los reportes convierten datos en información útil para tomar decisiones.
El dashboard hace más fácil interpretar los resultados porque los presenta visualmente.
Trabajar en VS Code ayudó a ejecutar, revisar y organizar todo el proyecto desde un solo entorno.
Este conocimiento puede aplicarse en una tienda, un colegio o una oficina para ordenar datos reales.
En resumen, la actividad me mostró cómo un programa puede ahorrar tiempo y mejorar el control de la información.
