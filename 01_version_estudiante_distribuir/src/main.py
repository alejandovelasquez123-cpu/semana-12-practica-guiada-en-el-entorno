from __future__ import annotations

import argparse
from pathlib import Path
from finca_auto.lector_csv import leer_csv
from finca_auto.validador import validar_registros
from finca_auto.analizador import analizar_produccion
from finca_auto.reportes import generar_reporte_txt, generar_resumen_json
from finca_auto.backup import crear_respaldo
from finca_auto.dashboard import generar_dashboard
from finca_auto.logger import crear_logger
from finca_auto.config import ROOT, OUTPUTS_DIR


def construir_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automatiza reportes y respaldos de produccion rural."
    )
    parser.add_argument(
        "--data",
        default="data/produccion_finca.csv",
        help="Ruta del archivo CSV que se desea analizar."
    )
    parser.add_argument(
        "--modo",
        default="normal",
        choices=["normal", "reto"],
        help="Modo de ejecucion para la practica."
    )
    parser.add_argument(
        "--estricto",
        action="store_true",
        help="Si se activa, el programa se detiene cuando encuentra errores de validacion."
    )
    return parser.parse_args()


def resolver_ruta(ruta: str) -> Path:
    path = Path(ruta)
    if not path.is_absolute():
        path = ROOT / path
    return path


def main() -> int:
    args = construir_argumentos()
    archivo_datos = resolver_ruta(args.data)
    logger = crear_logger(OUTPUTS_DIR / "logs")

    print("\n" + "=" * 72)
    print("SEMANA 12 - AUTOMATIZACION DE RESPALDOS Y REPORTES")
    print("=" * 72)
    print(f"Archivo de datos: {archivo_datos}")
    print(f"Modo: {args.modo}")

    logger.info("Inicio de ejecucion")
    logger.info("Archivo de datos: %s", archivo_datos)

    if not archivo_datos.exists():
        print("ERROR: No se encontro el archivo de datos.")
        print("Verifica la ruta y vuelve a ejecutar el comando.")
        logger.error("Archivo no encontrado: %s", archivo_datos)
        return 1

    try:
        registros_crudos = leer_csv(archivo_datos)
    except Exception as exc:
        print(f"ERROR al leer el CSV: {exc}")
        logger.exception("Error al leer CSV")
        return 1

    validos, problemas = validar_registros(registros_crudos)

    if problemas:
        print("\nSe detectaron problemas de validacion:")
        for problema in problemas:
            print(f"- Fila {problema.fila}: {problema.campo} -> {problema.mensaje}")
        logger.warning("Problemas de validacion detectados: %s", len(problemas))
        if args.estricto:
            print("\nModo estricto activado: el programa se detiene por errores de datos.")
            return 2
    else:
        print("\nValidacion completada: no se encontraron errores en los datos.")

    if not validos:
        print("\nNo hay registros validos para analizar. Revisa el archivo CSV.")
        return 3

    resultado = analizar_produccion(validos, problemas)

    reporte_txt = generar_reporte_txt(resultado, archivo_datos, OUTPUTS_DIR / "reportes")
    resumen_json = generar_resumen_json(resultado, archivo_datos, OUTPUTS_DIR / "reportes")
    respaldo = crear_respaldo(archivo_datos, OUTPUTS_DIR / "respaldos")
    dashboard = generar_dashboard(resultado, validos, OUTPUTS_DIR / "dashboard")

    logger.info("Reporte TXT generado: %s", reporte_txt)
    logger.info("Resumen JSON generado: %s", resumen_json)
    logger.info("Respaldo creado: %s", respaldo)
    logger.info("Dashboard generado: %s", dashboard)
    logger.info("Fin de ejecucion")

    print("\nResultados generados:")
    print(f"- Reporte TXT: {reporte_txt}")
    print(f"- Resumen JSON: {resumen_json}")
    print(f"- Respaldo CSV: {respaldo}")
    print(f"- Dashboard HTML: {dashboard}")

    print("\nResumen rapido:")
    print(f"- Registros validos: {resultado['registros_validos']}")
    print(f"- Problemas detectados: {resultado['problemas_detectados']}")
    print(f"- Total leche: {resultado['total_leche_litros']} litros")
    print(f"- Promedio diario leche: {resultado['promedio_leche_litros']} litros")
    print(f"- Total maiz: {resultado['total_maiz_kg']} kg")
    print(f"- Alertas: {len(resultado['alertas'])}")

    print("\nAbre el dashboard en el navegador:")
    print("outputs/dashboard/index.html")
    print("=" * 72 + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
