import pytest
from insercion import (
    insertar_al_inicio,
    insertar_al_final,
    insertar_en_posicion,
    insertar_ordenado,
    insertar_varios,
)


def test_insertar_al_inicio():
    assert insertar_al_inicio([2, 3, 4], 1) == [1, 2, 3, 4]


def test_insertar_al_inicio_vacia():
    assert insertar_al_inicio([], 1) == [1]


def test_insertar_al_final():
    assert insertar_al_final([1, 2, 3], 4) == [1, 2, 3, 4]


def test_insertar_al_final_vacia():
    assert insertar_al_final([], 1) == [1]


def test_insertar_en_posicion_medio():
    assert insertar_en_posicion([1, 2, 4, 5], 3, 2) == [1, 2, 3, 4, 5]


def test_insertar_en_posicion_inicio():
    assert insertar_en_posicion([1, 2, 3], 0, 0) == [0, 1, 2, 3]


def test_insertar_en_posicion_final():
    assert insertar_en_posicion([1, 2, 3], 4, 10) == [1, 2, 3, 4]


def test_insertar_en_posicion_negativa():
    assert insertar_en_posicion([1, 2, 3, 5], 4, -1) == [1, 2, 3, 4, 5]


def test_insertar_ordenado():
    assert insertar_ordenado([1, 3, 5, 7], 4) == [1, 3, 4, 5, 7]


def test_insertar_ordenado_inicio():
    assert insertar_ordenado([2, 3, 4], 1) == [1, 2, 3, 4]


def test_insertar_ordenado_final():
    assert insertar_ordenado([1, 2, 3], 4) == [1, 2, 3, 4]


def test_insertar_varios():
    assert insertar_varios([1, 5, 6], [2, 3, 4], 1) == [1, 2, 3, 4, 5, 6]


def test_insertar_varios_final():
    assert insertar_varios([1, 2], [3, 4], 10) == [1, 2, 3, 4]
