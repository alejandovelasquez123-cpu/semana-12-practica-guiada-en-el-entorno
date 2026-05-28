from __future__ import annotations

from datetime import datetime
from .config import COLUMNAS_OBLIGATORIAS
from .modelos import ProblemaValidacion

NUMERICOS = ["leche_litros", "maiz_kg", "alimento_kg", "lluvia_mm"]


def _convertir_float(valor: str, campo: str, numero_fila: int, problemas: list[ProblemaValidacion]) -> float | None:
    if valor is None or str(valor).strip() == "":
        problemas.append(ProblemaValidacion(numero_fila, campo, "El valor esta vacio", valor))
        return None
    try:
        numero = float(str(valor).replace(",", "."))
    except ValueError:
        problemas.append(ProblemaValidacion(numero_fila, campo, "Debe ser numerico", valor))
        return None
    if numero < 0:
        problemas.append(ProblemaValidacion(numero_fila, campo, "No puede ser negativo", valor))
        return None
    return numero


def _validar_fecha(valor: str, numero_fila: int, problemas: list[ProblemaValidacion]) -> bool:
    if valor is None or str(valor).strip() == "":
        problemas.append(ProblemaValidacion(numero_fila, "fecha", "La fecha esta vacia", valor))
        return False
    try:
        datetime.strptime(valor, "%Y-%m-%d")
        return True
    except ValueError:
        problemas.append(ProblemaValidacion(numero_fila, "fecha", "Formato invalido. Usa YYYY-MM-DD", valor))
        return False


def validar_registros(registros: list[dict[str, str]]) -> tuple[list[dict], list[ProblemaValidacion]]:
    """Valida registros crudos y devuelve registros limpios y problemas encontrados."""
    problemas: list[ProblemaValidacion] = []
    validos: list[dict] = []

    for indice, registro in enumerate(registros, start=2):
        fila_valida = True

        for columna in COLUMNAS_OBLIGATORIAS:
            if columna not in registro:
                problemas.append(ProblemaValidacion(indice, columna, "Columna obligatoria faltante", None))
                fila_valida = False

        if not _validar_fecha(registro.get("fecha", ""), indice, problemas):
            fila_valida = False

        responsable = str(registro.get("responsable", "")).strip()
        if not responsable:
            problemas.append(ProblemaValidacion(indice, "responsable", "El responsable esta vacio", responsable))
            fila_valida = False

        convertido = dict(registro)
        for campo in NUMERICOS:
            numero = _convertir_float(registro.get(campo, ""), campo, indice, problemas)
            if numero is None:
                fila_valida = False
            else:
                convertido[campo] = numero

        if fila_valida:
            validos.append(convertido)

    return validos, problemas
