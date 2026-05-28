# Semana 12 - Práctica guiada en VS Code
## Scripts, automatización de respaldos y reportes

Bienvenido a esta práctica. En esta actividad vas a trabajar como estudiante técnico encargado de apoyar la gestión de información de una finca rural. La finca registra datos diarios de producción y necesita automatizar tres tareas que normalmente se hacen a mano:

1. Revisar datos.
2. Generar reportes.
3. Crear respaldos.

La práctica se desarrolla en **Visual Studio Code** usando **Python**. También vas a revisar archivos CSV, reportes TXT, resúmenes JSON, logs y un dashboard HTML.

---

## 1. Qué vas a aprender

Al finalizar, debes ser capaz de explicar y demostrar:

- Qué es un script y por qué se usa para automatizar tareas.
- Cómo se ejecuta un programa desde la terminal de VS Code.
- Qué diferencia hay entre datos de entrada, procesamiento y resultados.
- Cómo se genera un reporte a partir de datos organizados.
- Por qué los respaldos son importantes para proteger información.
- Cómo identificar errores comunes en archivos de datos.
- Cómo documentar evidencias mediante una bitácora técnica.
- Cómo presentar resultados de una práctica de programación.

---

## 2. Idea central de la práctica

Un programa útil no solo debe funcionar. También debe permitir que otra persona entienda qué hizo, con qué datos trabajó y qué resultados produjo.

En esta práctica el flujo será:

```text
Archivo CSV con datos de producción
        ↓
Script en Python
        ↓
Validación de datos
        ↓
Cálculos de totales, promedios y alertas
        ↓
Reporte TXT + resumen JSON + dashboard HTML
        ↓
Respaldo automático del archivo original
        ↓
Bitácora con capturas y análisis
```

---

## 3. Tecnologías usadas

| Tecnología | Para qué se usa |
|---|---|
| Python 3 | Lenguaje principal para automatizar el proceso. |
| CSV | Formato sencillo para almacenar datos tabulares. |
| JSON | Formato para guardar un resumen estructurado de resultados. |
| HTML/CSS/JavaScript | Presentación visual de resultados en un dashboard. |
| Markdown | Guías, bitácora, taller y documentación. |
| VS Code | Entorno donde se abre, ejecuta y analiza el proyecto. |
| Git/GitHub | Control de versiones si el docente solicita subir el proyecto. |

---

## 4. Estructura del proyecto

```text
semana12-practica-premium/
│
├── data/
│   ├── produccion_finca.csv
│   ├── produccion_finca_con_errores.csv
│   └── produccion_finca_reto.csv
│
├── docs/
│   ├── 01_LECTURA_GUIADA.md
│   ├── 02_GUIA_TERMINAL_VSCODE.md
│   ├── 03_EXPLICACION_DEL_CODIGO.md
│   ├── 04_RESPALDOS_Y_REPORTES.md
│   ├── 05_ERRORES_FRECUENTES.md
│   └── 06_ARQUITECTURA_DEL_PROYECTO.md
│
├── ejercicios_estudiante/
│   ├── 01_EXPLORAR_EL_PROYECTO.md
│   ├── 02_EJECUTAR_Y_OBSERVAR.md
│   ├── 03_ANALIZAR_ERRORES.md
│   ├── 04_MODIFICAR_DATOS.md
│   ├── 05_RETO_DE_MEJORA.md
│   └── RETO_EDITABLE_ESTUDIANTE.py
│
├── outputs/
│   ├── dashboard/
│   ├── logs/
│   ├── reportes/
│   └── respaldos/
│
├── presentacion_estudiante/
│   └── index.html
│
├── src/
│   ├── main.py
│   ├── diagnostico_entorno.py
│   └── finca_auto/
│       ├── analizador.py
│       ├── backup.py
│       ├── config.py
│       ├── dashboard.py
│       ├── lector_csv.py
│       ├── logger.py
│       ├── modelos.py
│       ├── reportes.py
│       └── validador.py
│
├── BITACORA_PLANTILLA.md
├── CHECKLIST_ENTREGA.md
├── GLOSARIO_TECNICO.md
├── GUIA_ESTUDIANTE_COMPLETA.md
├── INSTRUCCIONES_MOODLE.md
├── TALLER_PRACTICO.md
├── requirements.txt
└── .gitignore
```

---

## 5. Primeros comandos

Abre la terminal de VS Code y ejecuta primero:

```bash
python src/diagnostico_entorno.py
```

Si funciona, ejecuta el proyecto principal:

```bash
python src/main.py
```

Después prueba el archivo con errores:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

También puedes probar el dataset de reto:

```bash
python src/main.py --data data/produccion_finca_reto.csv --modo reto
```

---

## 6. Qué debe aparecer después de ejecutar

El programa debe crear o actualizar archivos en estas carpetas:

```text
outputs/reportes/     -> reportes en TXT y JSON
outputs/respaldos/    -> copias de seguridad del CSV
outputs/logs/         -> registro técnico de ejecución
outputs/dashboard/    -> dashboard visual en HTML
```

Abre este archivo en el navegador:

```text
outputs/dashboard/index.html
```

---

## 7. Consejo importante

No entregues solo capturas. Explica qué hiciste, qué viste y qué aprendiste. Esta práctica evalúa tanto la ejecución técnica como tu capacidad para analizar resultados.
