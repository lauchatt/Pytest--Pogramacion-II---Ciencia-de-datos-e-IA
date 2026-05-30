import pytest
from listas_enlazadas import ListaSimple, ListaDoble, ListaCircular


class TestListaSimple:
    def test_insertar_al_inicio(self):
        lista = ListaSimple()
        lista.insertar_al_inicio(3)
        lista.insertar_al_inicio(2)
        lista.insertar_al_inicio(1)
        assert lista.a_lista() == [1, 2, 3]

    def test_insertar_al_final(self):
        lista = ListaSimple()
        lista.insertar_al_final(1)
        lista.insertar_al_final(2)
        lista.insertar_al_final(3)
        assert lista.a_lista() == [1, 2, 3]

    def test_eliminar(self):
        lista = ListaSimple()
        for v in [1, 2, 3, 4]:
            lista.insertar_al_final(v)
        lista.eliminar(3)
        assert lista.a_lista() == [1, 2, 4]

    def test_eliminar_cabeza(self):
        lista = ListaSimple()
        lista.insertar_al_final(1)
        lista.insertar_al_final(2)
        lista.eliminar(1)
        assert lista.a_lista() == [2]

    def test_buscar(self):
        lista = ListaSimple()
        lista.insertar_al_final(10)
        lista.insertar_al_final(20)
        assert lista.buscar(10) is True
        assert lista.buscar(30) is False

    def test_lista_vacia(self):
        lista = ListaSimple()
        assert lista.a_lista() == []
        assert lista.buscar(1) is False


class TestListaDoble:
    def test_insertar_inicio_final(self):
        lista = ListaDoble()
        lista.insertar_al_inicio(2)
        lista.insertar_al_inicio(1)
        lista.insertar_al_final(3)
        assert lista.a_lista() == [1, 2, 3]

    def test_a_lista_reversa(self):
        lista = ListaDoble()
        for v in [1, 2, 3]:
            lista.insertar_al_final(v)
        assert lista.a_lista_reversa() == [3, 2, 1]

    def test_eliminar(self):
        lista = ListaDoble()
        for v in [1, 2, 3, 4]:
            lista.insertar_al_final(v)
        lista.eliminar(2)
        assert lista.a_lista() == [1, 3, 4]

    def test_eliminar_unico(self):
        lista = ListaDoble()
        lista.insertar_al_final(1)
        lista.eliminar(1)
        assert lista.a_lista() == []


class TestListaCircular:
    def test_insertar(self):
        lista = ListaCircular()
        lista.insertar(1)
        lista.insertar(2)
        lista.insertar(3)
        assert lista.a_lista() == [1, 2, 3]

    def test_buscar(self):
        lista = ListaCircular()
        lista.insertar(10)
        lista.insertar(20)
        assert lista.buscar(10) is True
        assert lista.buscar(30) is False

    def test_vacia(self):
        lista = ListaCircular()
        assert lista.a_lista() == []
        assert lista.buscar(1) is False
