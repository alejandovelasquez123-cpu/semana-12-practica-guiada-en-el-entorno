# Guía completa del estudiante
## Actividad 2 - Semana 12
### Práctica guiada en el entorno: scripts para tareas repetitivas, automatización de respaldos y reportes

---

# 1. Presentación de la actividad

En esta actividad vas a desarrollar una práctica guiada en Visual Studio Code. Trabajarás con un proyecto que simula una situación real: una finca rural necesita organizar sus datos de producción semanal y automatizar tareas que normalmente se hacen manualmente.

La práctica está diseñada para que comprendas el proceso paso a paso. No se espera que memorices código; se espera que puedas explicar qué hace cada parte del proyecto y por qué es útil.

---

# 2. Contexto del problema

Imagina la siguiente situación:

Una finca registra diariamente:

- Litros de leche producidos.
- Kilos de maíz cosechados.
- Kilos de alimento usados.
- Milímetros de lluvia.
- Responsable del registro.
- Observaciones del día.

Al final de la semana, el encargado debe calcular totales, promedios y revisar si hubo días con producción baja. Además, debe guardar una copia de seguridad de los datos para evitar pérdidas.

Si todo esto se hace manualmente, pueden presentarse problemas:

- Errores en sumas y promedios.
- Pérdida de archivos.
- Datos incompletos.
- Reportes desorganizados.
- Falta de evidencia del proceso.
- Dificultad para explicar resultados.

Por eso se usa un script.

---

# 3. Qué es un script en esta práctica

Un script es un archivo con instrucciones que el computador puede ejecutar. En esta práctica, el script principal está en:

```text
src/main.py
```

Ese archivo coordina varias acciones:

```text
1. Recibe la ruta del archivo CSV.
2. Lee los datos.
3. Revisa si existen errores.
4. Calcula indicadores.
5. Genera reportes.
6. Crea respaldos.
7. Construye un dashboard visual.
8. Registra lo ocurrido en un log.
```

Un script se parece a una lista de instrucciones, pero con una ventaja: puede repetirse muchas veces con rapidez y precisión.

---

# 4. Entrada, proceso y salida

Para entender cualquier programa, usa este modelo:

```text
ENTRADA -> PROCESO -> SALIDA
```

## Entrada

La entrada es la información que recibe el programa. En este proyecto, la entrada principal es:

```text
data/produccion_finca.csv
```

Ese archivo contiene datos organizados por columnas.

## Proceso

El proceso es lo que el programa hace con los datos. Por ejemplo:

- Leer filas.
- Convertir textos a números.
- Revisar valores negativos.
- Sumar litros de leche.
- Calcular promedios.
- Detectar alertas.
- Crear archivos de salida.

## Salida

La salida es lo que el programa produce. En esta práctica las salidas son:

- Reporte TXT.
- Resumen JSON.
- Dashboard HTML.
- Respaldo CSV.
- Log de ejecución.

---

# 5. Por qué se generan respaldos

Un respaldo es una copia de seguridad. Sirve para proteger la información original. Si alguien modifica accidentalmente el archivo, si se borra o si se daña, el respaldo permite recuperar una versión anterior.

En esta práctica, cada vez que ejecutes el script se crea una copia del archivo usado. El respaldo queda en:

```text
outputs/respaldos/
```

El nombre del archivo incluye fecha y hora para evitar sobrescribir respaldos anteriores.

Ejemplo:

```text
respaldo_produccion_finca_2026-05-27_153000.csv
```

Esto significa que el respaldo fue creado el 27 de mayo de 2026 a las 15:30:00.

---

# 6. Por qué se generan reportes

Un reporte resume información para que una persona pueda tomar decisiones. Los datos originales pueden tener muchas filas, pero el reporte responde preguntas concretas:

- ¿Cuánta leche se produjo en total?
- ¿Cuál fue el promedio diario?
- ¿Qué día tuvo mejor producción?
- ¿Qué día tuvo producción más baja?
- ¿Hubo datos incorrectos?
- ¿Qué alertas deben revisarse?

En esta práctica, el reporte queda en:

```text
outputs/reportes/
```

El reporte ayuda a convertir datos en información útil.

---

# 7. Qué es un dashboard

Un dashboard es una página visual que muestra resultados de manera más fácil de interpretar. En esta práctica se genera un archivo HTML:

```text
outputs/dashboard/index.html
```

Al abrirlo en el navegador, verás tarjetas, indicadores, una tabla y barras visuales. Esto permite presentar resultados de forma más clara que solo con texto.

---

# 8. Qué significa validar datos

Validar datos significa revisar si la información tiene sentido antes de usarla.

Ejemplos de datos problemáticos:

```text
Fecha vacía
Litros de leche negativos
Texto donde debería haber un número
Fila incompleta
Responsable vacío
```

Un programa responsable no debe confiar ciegamente en los datos. Primero debe revisarlos. Por eso este proyecto incluye un archivo con errores:

```text
data/produccion_finca_con_errores.csv
```

Cuando ejecutes ese archivo, el programa debe mostrar advertencias o errores para que analices qué ocurrió.

---

# 9. Paso a paso de la práctica

## Paso 1. Abrir el proyecto

1. Descomprime el ZIP.
2. Abre Visual Studio Code.
3. Selecciona **File > Open Folder**.
4. Abre la carpeta del proyecto.
5. Verifica que puedas ver `data`, `src`, `docs`, `outputs` y `ejercicios_estudiante`.

Evidencia: captura de pantalla del proyecto abierto.

## Paso 2. Leer la guía inicial

Lee:

```text
README.md
GUIA_ESTUDIANTE_COMPLETA.md
```

No necesitas memorizar todo. El objetivo es ubicarte.

## Paso 3. Revisar los datos

Abre:

```text
data/produccion_finca.csv
```

Observa las columnas. Responde en tu bitácora:

- ¿Qué datos registra la finca?
- ¿Qué columna parece más importante?
- ¿Qué columna podría generar errores si queda vacía?

## Paso 4. Ejecutar diagnóstico

En la terminal de VS Code ejecuta:

```bash
python src/diagnostico_entorno.py
```

El diagnóstico revisa si Python está funcionando y si existen las carpetas principales.

## Paso 5. Ejecutar script principal

Ejecuta:

```bash
python src/main.py
```

Observa los mensajes de la terminal. No cierres la terminal inmediatamente. Lee qué archivos se generaron.

## Paso 6. Revisar salidas

Abre las carpetas:

```text
outputs/reportes/
outputs/respaldos/
outputs/logs/
outputs/dashboard/
```

Responde:

- ¿Qué archivos se crearon?
- ¿Cuál parece ser el reporte principal?
- ¿Cuál es el respaldo?
- ¿Para qué sirve el log?

## Paso 7. Abrir dashboard

Abre:

```text
outputs/dashboard/index.html
```

Puedes hacer doble clic o abrirlo desde el navegador.

Evidencia: captura del dashboard.

## Paso 8. Probar datos con errores

Ejecuta:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

Analiza los mensajes.

Responde:

- ¿Qué errores o advertencias aparecieron?
- ¿Por qué esos errores son importantes?
- ¿El programa pudo continuar o se detuvo?

## Paso 9. Modificar datos

Abre `data/produccion_finca.csv` y cambia un valor. Por ejemplo, cambia la producción de leche de un día.

Ejecuta otra vez:

```bash
python src/main.py
```

Compara el nuevo reporte con el anterior.

Responde:

- ¿Qué indicador cambió?
- ¿Por qué cambió?
- ¿Qué aprendiste sobre datos de entrada y resultados?

## Paso 10. Resolver el reto de mejora

Abre:

```text
ejercicios_estudiante/05_RETO_DE_MEJORA.md
```

El reto te pedirá proponer una mejora al sistema. Puede ser una nueva alerta, una columna nueva o una mejora visual.

---

# 10. Errores frecuentes y cómo actuar

## Error: python no se reconoce

Prueba:

```bash
py src/main.py
```

O:

```bash
python3 src/main.py
```

## Error: no such file or directory

Verifica que estés en la carpeta raíz del proyecto. Debes ver `README.md`, `data` y `src`.

## Error en CSV

Revisa que no hayas borrado comas ni encabezados.

## No aparece el dashboard

Ejecuta nuevamente:

```bash
python src/main.py
```

Luego revisa:

```text
outputs/dashboard/index.html
```

---

# 11. Qué debes entregar

Debes entregar en Moodle:

1. Bitácora completa.
2. Captura del proyecto abierto en VS Code.
3. Captura de la terminal ejecutando el script.
4. Captura del reporte generado.
5. Captura del respaldo generado.
6. Captura del dashboard.
7. Respuestas del taller.
8. Conclusión personal.

---

# 12. Cómo escribir una buena conclusión

Una conclusión débil dice:

```text
Aprendí a ejecutar el programa.
```

Una conclusión fuerte dice:

```text
Aprendí que un script permite automatizar tareas repetitivas como calcular totales, generar reportes y crear respaldos. También comprendí que validar datos es importante porque un dato incorrecto puede afectar todos los resultados. Esta práctica puede aplicarse en una finca, tienda o institución educativa para organizar información y evitar pérdida de archivos.
```

---

# 13. Pregunta final para reflexionar

Si tuvieras que aplicar este sistema en otro contexto, por ejemplo una tienda, una biblioteca o una institución educativa, ¿qué datos registrarías y qué reporte automático generarías?
