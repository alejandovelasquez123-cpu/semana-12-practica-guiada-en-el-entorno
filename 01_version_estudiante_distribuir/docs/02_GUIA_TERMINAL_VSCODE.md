# Guía de terminal en VS Code

## 1. Qué es la terminal

La terminal es una herramienta donde escribes comandos para ejecutar programas, moverte entre carpetas y observar mensajes técnicos.

En esta práctica la usarás para ejecutar Python.

---

## 2. Cómo abrir la terminal

En VS Code puedes abrirla de estas formas:

- Menú superior: **Terminal > New Terminal**.
- Atajo común: `Ctrl + Ñ` o `Ctrl + Shift + P` y buscar `Terminal`.

---

## 3. Cómo saber si estás en la carpeta correcta

Debes estar en la carpeta donde están `README.md`, `data` y `src`.

Puedes revisar con:

```bash
ls
```

En PowerShell también puedes usar:

```powershell
dir
```

Si ves estas carpetas, estás bien:

```text
data
src
docs
outputs
```

---

## 4. Comandos de esta práctica

Diagnóstico:

```bash
python src/diagnostico_entorno.py
```

Ejecución principal:

```bash
python src/main.py
```

Ejecución con archivo de errores:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

Ejecución con archivo de reto:

```bash
python src/main.py --data data/produccion_finca_reto.csv --modo reto
```

---

## 5. Si `python` no funciona

Prueba:

```bash
py src/main.py
```

O:

```bash
python3 src/main.py
```

Depende de cómo esté instalado Python en tu computador.

---

## 6. Cómo leer los mensajes

No ignores la terminal. Allí el programa puede mostrar:

- Archivos leídos.
- Errores encontrados.
- Reportes generados.
- Respaldos creados.
- Rutas de salida.

Leer la terminal hace parte del trabajo técnico.
