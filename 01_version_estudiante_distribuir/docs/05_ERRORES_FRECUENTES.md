# Errores frecuentes y cómo resolverlos

## 1. Error: `python` no se reconoce

Causa posible: Python no está agregado al PATH o se usa otro comando.

Solución:

```bash
py src/main.py
```

O:

```bash
python3 src/main.py
```

---

## 2. Error: archivo no encontrado

Causa posible: estás ejecutando el comando desde otra carpeta.

Solución: verifica que estés en la carpeta raíz del proyecto.

---

## 3. Error: CSV dañado

Causa posible: se borraron encabezados, comas o columnas.

Solución: compara con el archivo original o vuelve a descomprimir el ZIP.

---

## 4. El dashboard no abre

Causa posible: el script no se ejecutó correctamente o no se generó `index.html`.

Solución:

```bash
python src/main.py
```

Luego abre:

```text
outputs/dashboard/index.html
```

---

## 5. No aparecen reportes

Causa posible: el programa se detuvo por errores graves o no tienes permisos de escritura.

Solución: lee la terminal y revisa la carpeta `outputs/logs`.

---

## 6. Error al modificar datos

Causa posible: escribiste texto donde debía ir un número.

Ejemplo incorrecto:

```text
muchos
```

Ejemplo correcto:

```text
25.5
```

---

## 7. Consejo técnico

Cuando aparezca un error, no lo borres sin leerlo. El mensaje de error suele indicar el archivo, la línea o el tipo de problema.
