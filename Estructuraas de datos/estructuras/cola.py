"""
Cola (FIFO) con metodos basicos.
"""


class Cola:
    """Representa una cola (FIFO)."""

    def __init__(self):
        self._datos = []

    def enqueue(self, valor):
        """Agrega un valor al final de la cola."""
        self._datos.append(valor)

    def dequeue(self):
        """
        Saca y retorna el elemento del frente.
        Si esta vacia, muestra un mensaje y retorna None.
        """
        if self.esta_vacia():
            print("La cola esta vacia. No se puede hacer dequeue.")
            return None
        return self._datos.pop(0)

    def front(self):
        """
        Retorna el elemento del frente sin eliminarlo.
        Si esta vacia, muestra un mensaje y retorna None.
        """
        if self.esta_vacia():
            print("La cola esta vacia. No hay frente.")
            return None
        return self._datos[0]

    def esta_vacia(self):
        """Retorna True si la cola esta vacia."""
        return len(self._datos) == 0

    def tamano(self):
        """Retorna el tamano de la cola."""
        return len(self._datos)

    def mostrar(self):
        """Retorna una representacion bonita de la cola."""
        return "Cola: [" + ", ".join(str(x) for x in self._datos) + "]"
