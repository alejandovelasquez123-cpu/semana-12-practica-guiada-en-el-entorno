"""
Reto editable del estudiante
Semana 12 - Scripts, respaldos y reportes

Instrucción:
Lee esta función y completa una mejora sencilla.
No es obligatorio que sea perfecta. Lo importante es explicar la lógica.
"""


def generar_alerta_personalizada(registro):
    """
    Recibe un registro de producción y retorna una alerta si detecta una condición especial.

    Ideas:
    - Si la lluvia es muy alta, retornar una alerta.
    - Si la leche es muy baja, retornar una alerta.
    - Si el maíz cosechado es cero, retornar una alerta.

    Parámetro:
        registro: diccionario con datos de un día.

    Retorna:
        texto con alerta o None si no hay alerta.
    """

    # TODO ESTUDIANTE:
    # 1. Lee el valor de lluvia_mm, leche_litros o maiz_kg.
    # 2. Crea una condición.
    # 3. Retorna un mensaje claro si se cumple la condición.
    # 4. Si no hay alerta, retorna None.

    return None


# Ejemplo de prueba manual
if __name__ == "__main__":
    ejemplo = {
        "fecha": "2026-05-20",
        "leche_litros": 18,
        "maiz_kg": 30,
        "lluvia_mm": 65,
    }

    alerta = generar_alerta_personalizada(ejemplo)
    print("Alerta generada:", alerta)
