"""
Ejercicio 1: Tipos de Datos
Practica con tipos básicos: int, float, str, bool, list, tuple, dict, set.
"""


def operaciones_basicas(a: int, b: int) -> dict:
    """Recibe dos enteros, retorna un dict con suma, resta, multiplicación,
    división y módulo. Si b es 0, división y módulo retornan None."""
    return {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b if b != 0 else None,
        "modulo": a % b if b != 0 else None,
    }


def convertir_tipos(valor: str) -> dict:
    """Recibe un string numérico (ej. "42"). Retorna dict con int, float,
    str y bool."""
    return {
        "int": int(valor),
        "float": float(valor),
        "str": valor,
        "bool": bool(int(valor)),
    }


def manipular_lista(numeros: list) -> dict:
    """Retorna dict con primero, último, reverso y ordenado de una lista."""
    if not numeros:
        return {"primero": None, "ultimo": None, "reverso": [], "ordenado": []}
    return {
        "primero": numeros[0],
        "ultimo": numeros[-1],
        "reverso": list(reversed(numeros)),
        "ordenado": sorted(numeros, reverse=False),
    }


def operar_conjuntos(a: set, b: set) -> dict:
    """Retorna unión, intersección, diferencia y diferencia simétrica."""
    return {
        "union": a | b,
        "interseccion": a & b,
        "diferencia": a - b,
        "diferencia_simetrica": a ^ b,
    }


def contar_caracteres(texto: str) -> dict:
    """Cuenta frecuencia de cada caracter. Retorna dict {char: count}."""
    frecuencias = {}
    for c in texto:
        frecuencias[c] = frecuencias.get(c, 0) + 1
    return frecuencias
