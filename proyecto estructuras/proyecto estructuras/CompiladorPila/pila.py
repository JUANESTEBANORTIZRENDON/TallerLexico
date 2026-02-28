from __future__ import annotations
from typing import Generic, List, TypeVar

T = TypeVar("T")


class Pila(Generic[T]):
    """
    Pila LIFO: Last-In First-Out.
    Importante en máquinas de pila: operandos y resultados viven aquí.
    """
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Pila vacía: no se puede hacer pop()")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Pila vacía: no se puede hacer peek()")
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Pila({self._items})"