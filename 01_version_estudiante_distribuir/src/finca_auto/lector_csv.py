from __future__ import annotations

import csv
from pathlib import Path


def leer_csv(ruta: Path) -> list[dict[str, str]]:
    """Lee un archivo CSV y retorna una lista de diccionarios."""
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames is None:
            raise ValueError("El archivo CSV no tiene encabezados.")
        return [dict(fila) for fila in lector]
