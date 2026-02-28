"""
Arbol binario de busqueda (BST) con recorridos.
"""


class Nodo:
    """Nodo del arbol binario."""

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    """Arbol binario de busqueda (BST)."""

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un valor en el arbol (BST)."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        return self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
                return True
            return self._insertar_rec(nodo.izquierdo, valor)
        if valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
                return True
            return self._insertar_rec(nodo.derecho, valor)
        print("Valor duplicado. No se inserta:", valor)
        return False

    def buscar(self, valor):
        """Retorna True si el valor existe en el arbol."""
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izquierdo, valor)
        return self._buscar_rec(nodo.derecho, valor)

    def preorden(self):
        """Retorna una lista con el recorrido en preorden."""
        resultado = []
        self._preorden_rec(self.raiz, resultado)
        return resultado

    def _preorden_rec(self, nodo, resultado):
        if nodo is None:
            return
        resultado.append(nodo.valor)
        self._preorden_rec(nodo.izquierdo, resultado)
        self._preorden_rec(nodo.derecho, resultado)

    def inorden(self):
        """Retorna una lista con el recorrido en inorden."""
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden_rec(nodo.izquierdo, resultado)
        resultado.append(nodo.valor)
        self._inorden_rec(nodo.derecho, resultado)

    def postorden(self):
        """Retorna una lista con el recorrido en postorden."""
        resultado = []
        self._postorden_rec(self.raiz, resultado)
        return resultado

    def _postorden_rec(self, nodo, resultado):
        if nodo is None:
            return
        self._postorden_rec(nodo.izquierdo, resultado)
        self._postorden_rec(nodo.derecho, resultado)
        resultado.append(nodo.valor)

    def mostrar_recorridos(self):
        """Imprime los recorridos preorden, inorden y postorden."""
        if self.raiz is None:
            print("El arbol esta vacio.")
            return
        print("Preorden :", self.preorden())
        print("Inorden  :", self.inorden())
        print("Postorden:", self.postorden())
