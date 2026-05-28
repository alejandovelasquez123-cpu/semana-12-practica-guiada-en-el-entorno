from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil


def crear_respaldo(archivo_origen: Path, carpeta_respaldo: Path) -> Path:
    carpeta_respaldo.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    nombre = f"respaldo_{archivo_origen.stem}_{timestamp}{archivo_origen.suffix}"
    destino = carpeta_respaldo / nombre
    shutil.copy2(archivo_origen, destino)
    return destino
