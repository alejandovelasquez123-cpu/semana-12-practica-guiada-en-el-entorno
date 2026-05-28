from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS_DIR = ROOT / "outputs"

COLUMNAS_OBLIGATORIAS = [
    "fecha",
    "dia",
    "leche_litros",
    "maiz_kg",
    "alimento_kg",
    "lluvia_mm",
    "responsable",
    "observacion",
]

# Umbrales usados para generar alertas.
# Puedes analizarlos en el reto de mejora.
UMBRAL_LECHE_BAJA = 22.0
UMBRAL_LLUVIA_ALTA = 50.0
UMBRAL_ALIMENTO_ALTO = 14.0
