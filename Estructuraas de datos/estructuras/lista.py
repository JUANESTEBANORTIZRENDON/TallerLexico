"""
Lista ordenada (ascendente) con metodos basicos.
"""

import bisect

class Lista:
    """
    Representa una lista ordenada (ascendente).

    Idea clave:
    - La lista SIEMPRE se mantiene ordenada.
    - Por eso, la insercion se hace por valor (no por indice).
    """

    def __init__(self):
        self._datos = []

    def agregar_al_final(self, valor):
        """
        Alias didactico para mantener compatibilidad.

        En una lista ordenada, "agregar al final" no tiene sentido como operacion
        que preserve el orden; aqui se interpreta como insertar manteniendo el orden.
        """
        return self.insertar(valor)

    def insertar(self, valor):
        """Inserta un valor y mantiene la lista ordenada (ascendente)."""
        indice = bisect.bisect_right(self._datos, valor)
        self._datos.insert(indice, valor)
        return True

    def insertar_en(self, indice, valor):
        """
        En una lista ordenada no se recomienda insertar por indice porque rompe el orden.

        Se deja el metodo solo para explicar el error y guiar al estudiante.
        """
        print("Operacion no permitida: Lista ordenada no inserta por indice.")
        print("Usa: insertar(valor) para mantener el orden.")
        return False

    def eliminar_en(self, indice):
        """
        Elimina el elemento en el indice dado y lo retorna.
        Si el indice es invalido, muestra un mensaje y retorna None.
        """
        if indice < 0 or indice >= len(self._datos):
            print("Indice invalido. Debe estar entre 0 y", len(self._datos) - 1)
            return None
        return self._datos.pop(indice)

    def buscar(self, valor):
        """
        Devuelve el indice del valor o -1 si no existe.

        Como la lista esta ordenada, se usa busqueda binaria.
        """
        indice = bisect.bisect_left(self._datos, valor)
        if indice < len(self._datos) and self._datos[indice] == valor:
            return indice
        return -1

    def obtener(self, indice):
        """
        Obtiene el elemento en el indice dado.
        Si el indice es invalido, muestra un mensaje y retorna None.
        """
        if indice < 0 or indice >= len(self._datos):
            print("Indice invalido. Debe estar entre 0 y", len(self._datos) - 1)
            return None
        return self._datos[indice]

    def mostrar(self):
        """Retorna una representacion bonita de la lista."""
        return "[" + ", ".join(str(x) for x in self._datos) + "]"

    def tamano(self):
        """Retorna el tamano de la lista."""
        return len(self._datos)
