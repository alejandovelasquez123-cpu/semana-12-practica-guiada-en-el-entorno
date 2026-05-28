from __future__ import annotations

from datetime import datetime
from pathlib import Path
import json


def _timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")


def generar_reporte_txt(resultado: dict, archivo_datos: Path, carpeta_salida: Path) -> Path:
    carpeta_salida.mkdir(parents=True, exist_ok=True)
    ruta = carpeta_salida / f"reporte_semanal_{_timestamp()}.txt"

    lineas = []
    lineas.append("REPORTE SEMANAL DE PRODUCCION RURAL")
    lineas.append("=" * 60)
    lineas.append(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lineas.append(f"Archivo analizado: {archivo_datos.name}")
    lineas.append("")
    lineas.append("1. RESUMEN GENERAL")
    lineas.append(f"- Registros validos: {resultado['registros_validos']}")
    lineas.append(f"- Problemas detectados: {resultado['problemas_detectados']}")
    lineas.append("")
    lineas.append("2. PRODUCCION DE LECHE")
    lineas.append(f"- Total semanal: {resultado['total_leche_litros']} litros")
    lineas.append(f"- Promedio diario: {resultado['promedio_leche_litros']} litros")
    lineas.append(f"- Mayor produccion: {resultado['mayor_leche']['dia']} ({resultado['mayor_leche']['leche_litros']} litros)")
    lineas.append(f"- Menor produccion: {resultado['menor_leche']['dia']} ({resultado['menor_leche']['leche_litros']} litros)")
    lineas.append("")
    lineas.append("3. COSECHA DE MAIZ")
    lineas.append(f"- Total semanal: {resultado['total_maiz_kg']} kg")
    lineas.append(f"- Promedio diario: {resultado['promedio_maiz_kg']} kg")
    lineas.append(f"- Mayor cosecha: {resultado['mayor_maiz']['dia']} ({resultado['mayor_maiz']['maiz_kg']} kg)")
    lineas.append("")
    lineas.append("4. ALIMENTO Y LLUVIA")
    lineas.append(f"- Total alimento usado: {resultado['total_alimento_kg']} kg")
    lineas.append(f"- Promedio alimento diario: {resultado['promedio_alimento_kg']} kg")
    lineas.append(f"- Total lluvia: {resultado['total_lluvia_mm']} mm")
    lineas.append(f"- Promedio lluvia diaria: {resultado['promedio_lluvia_mm']} mm")
    lineas.append("")
    lineas.append("5. TENDENCIA")
    lineas.append(f"- {resultado['tendencia']}")
    lineas.append("")
    lineas.append("6. ALERTAS")
    if resultado["alertas"]:
        for alerta in resultado["alertas"]:
            lineas.append(f"- {alerta}")
    else:
        lineas.append("- No se generaron alertas.")
    lineas.append("")
    lineas.append("7. OBSERVACION TECNICA")
    lineas.append("Este reporte fue generado automaticamente mediante un script de Python.")
    lineas.append("Revise siempre los datos de entrada antes de tomar decisiones.")

    ruta.write_text("\n".join(lineas), encoding="utf-8")
    return ruta


def generar_resumen_json(resultado: dict, archivo_datos: Path, carpeta_salida: Path) -> Path:
    carpeta_salida.mkdir(parents=True, exist_ok=True)
    ruta = carpeta_salida / f"resumen_semanal_{_timestamp()}.json"
    contenido = {
        "generado_en": datetime.now().isoformat(timespec="seconds"),
        "archivo_analizado": archivo_datos.name,
        "resultado": resultado,
    }
    ruta.write_text(json.dumps(contenido, ensure_ascii=False, indent=2), encoding="utf-8")
    return ruta
