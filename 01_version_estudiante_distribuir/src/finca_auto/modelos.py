from dataclasses import dataclass


@dataclass
class ProblemaValidacion:
    fila: int
    campo: str
    mensaje: str
    valor: str | None = None
