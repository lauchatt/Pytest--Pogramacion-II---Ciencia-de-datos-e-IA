import pytest
from ordenamiento import bubble_sort, selection_sort, insertion_sort, merge_sort


class TestOrdenamiento:
    @pytest.fixture
    def lista_ejemplo(self):
        return [64, 34, 25, 12, 22, 11, 90]

    @pytest.fixture
    def lista_ordenada(self):
        return [11, 12, 22, 25, 34, 64, 90]

    def test_bubble_sort(self, lista_ejemplo, lista_ordenada):
        assert bubble_sort(lista_ejemplo) == lista_ordenada

    def test_selection_sort(self, lista_ejemplo, lista_ordenada):
        assert selection_sort(lista_ejemplo) == lista_ordenada

    def test_insertion_sort(self, lista_ejemplo, lista_ordenada):
        assert insertion_sort(lista_ejemplo) == lista_ordenada

    def test_merge_sort(self, lista_ejemplo, lista_ordenada):
        assert merge_sort(lista_ejemplo) == lista_ordenada

    def test_lista_vacia(self):
        assert bubble_sort([]) == []
        assert selection_sort([]) == []
        assert insertion_sort([]) == []
        assert merge_sort([]) == []

    def test_lista_un_elemento(self):
        for sort_fn in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
            assert sort_fn([1]) == [1]

    def test_lista_duplicados(self):
        for sort_fn in [bubble_sort, selection_sort, insertion_sort, merge_sort]:
            assert sort_fn([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

    def test_no_modifica_original(self, lista_ejemplo):
        original = lista_ejemplo.copy()
        bubble_sort(lista_ejemplo)
        assert lista_ejemplo == original
