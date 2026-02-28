from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Any


class OpCode(Enum):
    # Cargar/Apilar valores
    PUSH_CONST = auto()   # Empuja una constante a la pila

    # Operaciones aritméticas (consumen 2 operandos y empujan 1 resultado)
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()

    # Variables / memoria (un mini “entorno”)
    STORE = auto()        # Guarda el tope de la pila en una variable
    LOAD = auto()         # Carga una variable y la empuja a la pila

    # Control básico
    PRINT = auto()        # Imprime el tope (sin sacarlo, o sacándolo; aquí lo sacamos)
    HALT = auto()         # Finaliza programa


@dataclass(frozen=True)
class Instruccion:
    """
    Representa una instrucción de un bytecode / IR.

    - opcode: el tipo de instrucción (ADD, LOAD, etc.)
    - arg: argumento opcional (ej: constante, nombre de variable)
    """
    opcode: OpCode
    arg: Optional[Any] = None

    def __str__(self) -> str:
        return f"{self.opcode.name}" + (f" {self.arg}" if self.arg is not None else "")