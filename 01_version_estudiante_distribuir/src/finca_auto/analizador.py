from __future__ import annotations

from .config import UMBRAL_LECHE_BAJA, UMBRAL_LLUVIA_ALTA, UMBRAL_ALIMENTO_ALTO
from .modelos import ProblemaValidacion


def _redondear(valor: float) -> float:
    return round(valor, 2)


def analizar_produccion(registros: list[dict], problemas: list[ProblemaValidacion]) -> dict:
    total_leche = sum(r["leche_litros"] for r in registros)
    total_maiz = sum(r["maiz_kg"] for r in registros)
    total_alimento = sum(r["alimento_kg"] for r in registros)
    total_lluvia = sum(r["lluvia_mm"] for r in registros)
    cantidad = len(registros)

    mayor_leche = max(registros, key=lambda r: r["leche_litros"])
    menor_leche = min(registros, key=lambda r: r["leche_litros"])
    mayor_maiz = max(registros, key=lambda r: r["maiz_kg"])

    alertas: list[str] = []
    for r in registros:
        if r["leche_litros"] < UMBRAL_LECHE_BAJA:
            alertas.append(f"{r['fecha']} ({r['dia']}): leche baja ({r['leche_litros']} litros).")
        if r["lluvia_mm"] > UMBRAL_LLUVIA_ALTA:
            alertas.append(f"{r['fecha']} ({r['dia']}): lluvia alta ({r['lluvia_mm']} mm).")
        if r["alimento_kg"] > UMBRAL_ALIMENTO_ALTO:
            alertas.append(f"{r['fecha']} ({r['dia']}): consumo alto de alimento ({r['alimento_kg']} kg).")

    primera_mitad = registros[: max(1, cantidad // 2)]
    segunda_mitad = registros[max(1, cantidad // 2):]
    promedio_primera = sum(r["leche_litros"] for r in primera_mitad) / len(primera_mitad)
    promedio_segunda = sum(r["leche_litros"] for r in segunda_mitad) / len(segunda_mitad) if segunda_mitad else promedio_primera

    if promedio_segunda > promedio_primera:
        tendencia = "La produccion de leche tiende a subir en la segunda parte del periodo."
    elif promedio_segunda < promedio_primera:
        tendencia = "La produccion de leche tiende a bajar en la segunda parte del periodo."
    else:
        tendencia = "La produccion de leche se mantiene estable."

    return {
        "registros_validos": cantidad,
        "problemas_detectados": len(problemas),
        "total_leche_litros": _redondear(total_leche),
        "promedio_leche_litros": _redondear(total_leche / cantidad),
        "total_maiz_kg": _redondear(total_maiz),
        "promedio_maiz_kg": _redondear(total_maiz / cantidad),
        "total_alimento_kg": _redondear(total_alimento),
        "promedio_alimento_kg": _redondear(total_alimento / cantidad),
        "total_lluvia_mm": _redondear(total_lluvia),
        "promedio_lluvia_mm": _redondear(total_lluvia / cantidad),
        "mayor_leche": mayor_leche,
        "menor_leche": menor_leche,
        "mayor_maiz": mayor_maiz,
        "alertas": alertas,
        "tendencia": tendencia,
        "problemas": [p.__dict__ for p in problemas],
    }
