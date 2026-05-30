"""
Ejercicio 2: Algoritmos de Ordenamiento
Implementa Bubble Sort, Selection Sort, Insertion Sort y Merge Sort.
"""


def bubble_sort(lista: list) -> list:
    """Ordena una copia de la lista usando Bubble Sort. O(n²)."""
    lista = lista.copy ()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def selection_sort(lista: list) -> list:
    """Ordena una copia de la lista usando Selection Sort. O(n²)."""
    if len(lista) <= 1:
        return lista
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


def insertion_sort(lista: list) -> list:
    """Ordena una copia de la lista usando Insertion Sort. O(n²)."""
    if len(lista) <= 1:
        return lista
    if len(lista) <= 1:
        return lista
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def merge_sort(lista: list) -> list:
    """Ordena una copia de la lista usando Merge Sort. O(n log n)."""
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return _merge(izquierda, derecha)


def _merge(izquierda: list, derecha: list) -> list:
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
