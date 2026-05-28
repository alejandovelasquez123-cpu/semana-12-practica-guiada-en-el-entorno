from src.finca_auto.analizador import analizar_produccion


def test_analizador_calcula_totales_basicos():
    registros = [
        {"fecha": "2026-01-01", "dia": "Lunes", "leche_litros": 10.0, "maiz_kg": 5.0, "alimento_kg": 2.0, "lluvia_mm": 0.0},
        {"fecha": "2026-01-02", "dia": "Martes", "leche_litros": 20.0, "maiz_kg": 15.0, "alimento_kg": 3.0, "lluvia_mm": 1.0},
    ]
    resultado = analizar_produccion(registros, [])
    assert resultado["total_leche_litros"] == 30.0
    assert resultado["promedio_leche_litros"] == 15.0
    assert resultado["total_maiz_kg"] == 20.0
