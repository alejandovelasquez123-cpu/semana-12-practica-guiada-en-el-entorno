# Ejercicio 5 - Reto de mejora

## Objetivo

Proponer una mejora al sistema de automatización.

## Opciones de reto

Elige una:

### Opción A. Nueva alerta

Propón una alerta cuando la lluvia sea mayor a cierto valor.

### Opción B. Nueva columna

Agrega una columna al CSV, por ejemplo `gasto_veterinario`, y explica cómo debería incluirse en el reporte.

### Opción C. Mejora visual

Propón una mejora al dashboard, por ejemplo colores, tabla más clara o una nueva tarjeta.

### Opción D. Nuevo contexto

Adapta la idea del proyecto a una tienda, biblioteca o institución educativa.

## Entrega

### Mejora elegida: Opción A - Nueva alerta de lluvia

1. **Qué mejora elegiste:**
   Agregar una alerta cuando la lluvia sea mayor a 50 mm. Esto ayudaría a la finca a identificar días con lluvia extrema que podrían afectar las actividades o la salud de los animales.

2. **Por qué es útil:**
   La lluvia excesiva puede causar problemas como encharcamiento, enfermedades en animales, o dificultad para realizar tareas. Una alerta automática permitiría a la finca reaccionar rápido, por ejemplo, moviendo animales a cobertizos o posponiendo actividades.

3. **Qué archivo modificarías:**
   Modificaría `src/finca_auto/analizador.py` en la función que calcula alertas. Agregaría una condición que revise si `lluvia_mm > 50` y genere una alerta automática.

4. **Qué resultado esperas obtener:**
   En el reporte y dashboard aparecería una alerta roja que diga: "⚠️ Lluvia extrema: XX mm. Riesgo de encharcamiento y afectación a actividades." en los días con lluvia alta.

5. **Qué dificultad podrías encontrar:**
   La dificultad podría ser:
   - Decidir el umbral correcto (¿50 mm es demasiado o muy poco para esta región?).
   - Entender dónde exactamente colocar la lógica de alerta.
   - Probar que la alerta funcione correctamente con diferentes valores.

### Código propuesto:

La mejora se implementó en el archivo `ejercicios_estudiante/SOLUCION_SUGERIDA_RETO.py`.

Ver archivo: `ejercicios_estudiante/SOLUCION_SUGERIDA_RETO.py` (3 opciones de implementación)

## Archivo opcional

Puedes abrir:

```text
ejercicio_estudiante/RETO_EDITABLE_ESTUDIANTE.py
```

Allí encontrarás un espacio para escribir una función de mejora.
