"""
Ejercicio 6: Algoritmos de Búsqueda
Implementa búsqueda lineal y binaria (iterativa y recursiva).
"""


def busqueda_lineal(lista: list, objetivo) -> int:
    """Busca objetivo en lista de forma lineal.
    Retorna el índice si existe, -1 si no."""
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria_iterativa(lista: list, objetivo) -> int:
    """Búsqueda binaria iterativa. Lista debe estar ordenada.
    Retorna el índice si existe, -1 si no."""
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # ← punto medio real
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # ← buscar a la derecha
        else:
            derecha = medio - 1   # ← buscar a la izquierda
    return -1


def busqueda_binaria_recursiva(
    lista: list, objetivo, izquierda: int = None, derecha: int = None
) -> int:
    """Búsqueda binaria recursiva. Lista debe estar ordenada.
    Retorna el índice si existe, -1 si no."""
    if izquierda is None:
        izquierda, derecha = 0, len(lista) - 1
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


def busqueda_lineal_con_ocurrencias(lista: list, objetivo) -> list[int]:
    """Retorna lista con todos los índices donde aparece objetivo."""
    return [i for i, v in enumerate(lista) if v == objetivo]
