"""
Lista enlazada simple (un solo enlace).

Caracteristicas:
- Cada nodo apunta al siguiente (siguiente).
- Acceso por indice requiere recorrer desde la cabeza (O(n)).
"""


class Nodo:
    """Nodo para lista enlazada simple."""

    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente


class ListaEnlazada:
    """Lista enlazada simple con operaciones basicas."""

    def __init__(self):
        self._cabeza = None
        self._tamano = 0

    def agregar_al_final(self, valor):
        """Agrega un valor al final de la lista."""
        nuevo = Nodo(valor)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._tamano = 1
            return True

        actual = self._cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo
        self._tamano += 1
        return True

    def insertar_en(self, indice, valor):
        """
        Inserta un valor en el indice dado.
        Si el indice es invalido, muestra un mensaje y no inserta.
        """
        if indice < 0 or indice > self._tamano:
            print("Indice invalido. Debe estar entre 0 y", self._tamano)
            return False

        if indice == 0:
            self._cabeza = Nodo(valor, self._cabeza)
            self._tamano += 1
            return True

        anterior = self._nodo_en(indice - 1)
        anterior.siguiente = Nodo(valor, anterior.siguiente)
        self._tamano += 1
        return True

    def eliminar_en(self, indice):
        """
        Elimina el elemento en el indice dado y lo retorna.
        Si el indice es invalido, muestra un mensaje y retorna None.
        """
        if indice < 0 or indice >= self._tamano:
            print("Indice invalido. Debe estar entre 0 y", self._tamano - 1)
            return None

        if indice == 0:
            eliminado = self._cabeza
            self._cabeza = self._cabeza.siguiente
            self._tamano -= 1
            return eliminado.valor

        anterior = self._nodo_en(indice - 1)
        eliminado = anterior.siguiente
        anterior.siguiente = eliminado.siguiente
        self._tamano -= 1
        return eliminado.valor

    def buscar(self, valor):
        """Devuelve el indice del valor o -1 si no existe."""
        actual = self._cabeza
        indice = 0
        while actual is not None:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def obtener(self, indice):
        """
        Obtiene el elemento en el indice dado.
        Si el indice es invalido, muestra un mensaje y retorna None.
        """
        if indice < 0 or indice >= self._tamano:
            print("Indice invalido. Debe estar entre 0 y", self._tamano - 1)
            return None
        return self._nodo_en(indice).valor

    def mostrar(self):
        """Retorna una representacion bonita de la lista."""
        valores = []
        actual = self._cabeza
        while actual is not None:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return "[" + " -> ".join(valores) + "]"

    def tamano(self):
        """Retorna el tamano de la lista."""
        return self._tamano

    def _nodo_en(self, indice):
        """Retorna el nodo en un indice valido (uso interno)."""
        actual = self._cabeza
        pasos = 0
        while pasos < indice:
            actual = actual.siguiente
            pasos += 1
        return actual

