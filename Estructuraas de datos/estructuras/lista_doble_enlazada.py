"""
Lista doblemente enlazada (doble enlace).

Caracteristicas:
- Cada nodo apunta al siguiente y al anterior.
- Permite recorrer en ambos sentidos.
- Inserciones/eliminaciones en medio pueden ser mas comodas si ya tienes el nodo.
"""


class NodoDoble:
    """Nodo para lista doblemente enlazada."""

    def __init__(self, valor, anterior=None, siguiente=None):
        self.valor = valor
        self.anterior = anterior
        self.siguiente = siguiente


class ListaDobleEnlazada:
    """Lista doblemente enlazada con operaciones basicas."""

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamano = 0

    def agregar_al_final(self, valor):
        """Agrega un valor al final de la lista."""
        nuevo = NodoDoble(valor)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._cola = nuevo
            self._tamano = 1
            return True

        nuevo.anterior = self._cola
        self._cola.siguiente = nuevo
        self._cola = nuevo
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

        if indice == self._tamano:
            return self.agregar_al_final(valor)

        if indice == 0:
            nuevo = NodoDoble(valor, anterior=None, siguiente=self._cabeza)
            if self._cabeza is not None:
                self._cabeza.anterior = nuevo
            self._cabeza = nuevo
            if self._cola is None:
                self._cola = nuevo
            self._tamano += 1
            return True

        nodo_actual = self._nodo_en(indice)
        nuevo = NodoDoble(valor, anterior=nodo_actual.anterior, siguiente=nodo_actual)
        nodo_actual.anterior.siguiente = nuevo
        nodo_actual.anterior = nuevo
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

        if self._tamano == 1:
            valor = self._cabeza.valor
            self._cabeza = None
            self._cola = None
            self._tamano = 0
            return valor

        if indice == 0:
            eliminado = self._cabeza
            self._cabeza = eliminado.siguiente
            self._cabeza.anterior = None
            self._tamano -= 1
            return eliminado.valor

        if indice == self._tamano - 1:
            eliminado = self._cola
            self._cola = eliminado.anterior
            self._cola.siguiente = None
            self._tamano -= 1
            return eliminado.valor

        eliminado = self._nodo_en(indice)
        eliminado.anterior.siguiente = eliminado.siguiente
        eliminado.siguiente.anterior = eliminado.anterior
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
        """Retorna una representacion bonita (de cabeza a cola)."""
        valores = []
        actual = self._cabeza
        while actual is not None:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return "[" + " <-> ".join(valores) + "]"

    def mostrar_reversa(self):
        """Retorna una representacion bonita (de cola a cabeza)."""
        valores = []
        actual = self._cola
        while actual is not None:
            valores.append(str(actual.valor))
            actual = actual.anterior
        return "[" + " <-> ".join(valores) + "]"

    def tamano(self):
        """Retorna el tamano de la lista."""
        return self._tamano

    def _nodo_en(self, indice):
        """Retorna el nodo en un indice valido (uso interno)."""
        if indice < self._tamano // 2:
            actual = self._cabeza
            pasos = 0
            while pasos < indice:
                actual = actual.siguiente
                pasos += 1
            return actual

        actual = self._cola
        pasos = self._tamano - 1
        while pasos > indice:
            actual = actual.anterior
            pasos -= 1
        return actual

