import pytest
from busqueda import (
    busqueda_lineal,
    busqueda_binaria_iterativa,
    busqueda_binaria_recursiva,
    busqueda_lineal_con_ocurrencias,
)


class TestBusqueda:
    @pytest.fixture
    def lista_ordenada(self):
        return [1, 3, 5, 7, 9, 11, 13, 15]

    @pytest.fixture
    def lista_desordenada(self):
        return [7, 2, 9, 1, 5, 3]

    def test_busqueda_lineal_encuentra(self, lista_desordenada):
        assert busqueda_lineal(lista_desordenada, 9) == 2

    def test_busqueda_lineal_no_encuentra(self, lista_desordenada):
        assert busqueda_lineal(lista_desordenada, 42) == -1

    def test_busqueda_lineal_primero(self, lista_desordenada):
        assert busqueda_lineal(lista_desordenada, 7) == 0

    def test_busqueda_lineal_ultimo(self, lista_desordenada):
        assert busqueda_lineal(lista_desordenada, 3) == 5

    def test_busqueda_binaria_iterativa_encuentra(self, lista_ordenada):
        assert busqueda_binaria_iterativa(lista_ordenada, 7) == 3

    def test_busqueda_binaria_iterativa_no_encuentra(self, lista_ordenada):
        assert busqueda_binaria_iterativa(lista_ordenada, 8) == -1

    def test_busqueda_binaria_iterativa_extremos(self, lista_ordenada):
        assert busqueda_binaria_iterativa(lista_ordenada, 1) == 0
        assert busqueda_binaria_iterativa(lista_ordenada, 15) == 7

    def test_busqueda_binaria_recursiva_encuentra(self, lista_ordenada):
        assert busqueda_binaria_recursiva(lista_ordenada, 7) == 3

    def test_busqueda_binaria_recursiva_no_encuentra(self, lista_ordenada):
        assert busqueda_binaria_recursiva(lista_ordenada, 8) == -1

    def test_busqueda_binaria_recursiva_extremos(self, lista_ordenada):
        assert busqueda_binaria_recursiva(lista_ordenada, 1) == 0
        assert busqueda_binaria_recursiva(lista_ordenada, 15) == 7

    def test_lista_vacia(self):
        assert busqueda_lineal([], 1) == -1
        assert busqueda_binaria_iterativa([], 1) == -1
        assert busqueda_binaria_recursiva([], 1) == -1

    def test_busqueda_lineal_con_ocurrencias(self):
        assert busqueda_lineal_con_ocurrencias([1, 2, 3, 2, 4, 2], 2) == [1, 3, 5]

    def test_busqueda_lineal_con_ocurrencias_sin_resultados(self):
        assert busqueda_lineal_con_ocurrencias([1, 2, 3], 4) == []
