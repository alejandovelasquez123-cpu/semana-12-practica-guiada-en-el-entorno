from __future__ import annotations

from datetime import datetime
from pathlib import Path
import logging


def crear_logger(carpeta_logs: Path) -> logging.Logger:
    carpeta_logs.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("semana12")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    archivo = carpeta_logs / f"ejecucion_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}.log"
    handler = logging.FileHandler(archivo, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
