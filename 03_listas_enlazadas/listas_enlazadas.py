"""
Ejercicio 3: Listas Enlazadas
Implementa lista simplemente enlazada, doblemente enlazada y circular.
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nodo = Nodo(valor)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo


    def insertar_al_final(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo


    def eliminar(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def buscar(self, valor) -> bool:
        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                return True

            actual = actual.siguiente

        return False

    def a_lista(self) -> list:
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_inicio(self, valor):
        nodo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nodo
            return
        nodo.siguiente = self.cabeza
        self.cabeza.anterior = nodo
        self.cabeza = nodo

    def insertar_al_final(self, valor):
        nodo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nodo
            return
        nodo.anterior = self.cola
        self.cola.siguiente = nodo
        self.cola = nodo

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente  
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente

    def a_lista(self) -> list:
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

    def a_lista_reversa(self) -> list:
        resultado = []
        actual = self.cola
        while actual:
            resultado.append(actual.valor)
            actual = actual.anterior
        return resultado


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nodo  # ← estaba "self.cabeda"
            nodo.siguiente = self.cabeza
            return
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        actual.siguiente = nodo
        nodo.siguiente = self.cabeza 

    def buscar(self, valor) -> bool:
        if self.cabeza is None:
            return False
        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def a_lista(self) -> list:
        resultado = []
        if self.cabeza is None:
            return resultado
        actual = self.cabeza
        while True:
            resultado.append(actual.valor)
            actual = actual.siguiente
            if actual == self.cabeza:  
                break
        return resultado
