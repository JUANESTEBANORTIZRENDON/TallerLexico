"""
Pila (LIFO) con metodos basicos.
"""


class Pila:
    """Representa una pila (LIFO)."""

    def __init__(self):
        self._datos = []

    def push(self, valor):
        """Agrega un valor a la cima de la pila."""
        self._datos.append(valor)

    def pop(self):
        """
        Saca y retorna el elemento de la cima.
        Si esta vacia, muestra un mensaje y retorna None.
        """
        if self.esta_vacia():
            print("La pila esta vacia. No se puede hacer pop.")
            return None
        return self._datos.pop()

    def peek(self):
        """
        Retorna el elemento de la cima sin eliminarlo.
        Si esta vacia, muestra un mensaje y retorna None.
        """
        if self.esta_vacia():
            print("La pila esta vacia. No hay cima.")
            return None
        return self._datos[-1]

    def esta_vacia(self):
        """Retorna True si la pila esta vacia."""
        return len(self._datos) == 0

    def tamano(self):
        """Retorna el tamano de la pila."""
        return len(self._datos)

    def mostrar(self):
        """Retorna una representacion bonita de la pila."""
        return "Pila: [" + ", ".join(str(x) for x in self._datos) + "]"
