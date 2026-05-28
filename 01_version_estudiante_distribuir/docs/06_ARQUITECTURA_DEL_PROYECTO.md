# Arquitectura del proyecto

## 1. Mapa general

```text
data/                  Datos de entrada
src/                   Código fuente
src/finca_auto/        Módulos internos del sistema
outputs/               Resultados generados
presentacion_estudiante/ Explicación visual del flujo
docs/                  Documentación técnica
ejercicios_estudiante/ Prácticas y retos
```

## 2. Flujo técnico

```text
produccion_finca.csv
        ↓
lector_csv.py
        ↓
validador.py
        ↓
analizador.py
        ↓
reportes.py + dashboard.py + backup.py
        ↓
outputs/
```

## 3. Ventajas de esta organización

- Facilita encontrar errores.
- Permite mejorar una parte sin cambiar todo.
- Ayuda a trabajar en equipo.
- Se parece más a la estructura de proyectos reales.
- Permite documentar mejor.

## 4. Pregunta para el estudiante

¿Por qué sería más difícil entender este proyecto si todo el código estuviera en un solo archivo de 500 líneas?
