class ArbolBinario:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.izquierda = None
            self.derecha = None

    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = self.Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = self.Nodo(valor)
            else:
                self._agregar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = self.Nodo(valor)
            else:
                self._agregar(valor, nodo.derecha)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

# Crear el árbol
arbol = ArbolBinario()
arbol.agregar(5)
arbol.agregar(3)
arbol.agregar(7)
arbol.agregar(2)
arbol.agregar(4)
arbol.agregar(6)
arbol.agregar(8)

print("Recorrido Preorden: ")
arbol.preorden()
