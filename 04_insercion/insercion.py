"""
Ejercicio 4: Inserción en Listas
Inserción al inicio, final, en posición n y en lista ordenada.
"""


def insertar_al_inicio(lista: list, valor) -> list:
    """Retorna nueva lista con valor insertado al inicio."""
    return [valor] + lista


def insertar_al_final(lista: list, valor) -> list:
    """Retorna nueva lista con valor insertado al final."""
    return lista + [valor]


def insertar_en_posicion(lista: list, valor, posicion: int) -> list:
    """Inserta valor en la posición dada.
    - Si posición es negativa, cuenta desde el final.
    - Si posición excede el largo, inserta al final.
    """
    return lista[:posicion] + [valor] + lista[posicion:]


def insertar_ordenado(lista: list, valor) -> list:
    """Inserta valor en lista ordenada (ascendente) manteniendo el orden."""
    for i, v in enumerate(lista):
        if valor < v:
            return lista[:i] + [valor] + lista[i:]
    return lista + [valor]


def insertar_varios(lista: list, valores: list, posicion: int) -> list:
    """Inserta múltiples valores en la posición dada."""
    return lista[:posicion] + valores + lista[posicion:]
