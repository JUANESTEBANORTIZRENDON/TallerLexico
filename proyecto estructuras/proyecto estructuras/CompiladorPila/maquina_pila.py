from __future__ import annotations
from typing import Dict, List, Any

from pila import Pila
from instrucciones import Instruccion, OpCode


class MaquinaPila:
    """
    Máquina virtual basada en pila:
    - stack: operandos/resultados
    - memoria: variables (entorno)
    - ip: instruction pointer (índice de instrucción actual)
    """
    def __init__(self) -> None:
        self.stack: Pila[Any] = Pila()
        self.memoria: Dict[str, Any] = {}
        self.ip: int = 0

    def ejecutar(self, programa: List[Instruccion]) -> None:
        self.ip = 0
        while self.ip < len(programa):
            inst = programa[self.ip]
            op = inst.opcode

            if op == OpCode.PUSH_CONST:
                self.stack.push(inst.arg)

            elif op == OpCode.ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a + b)

            elif op == OpCode.SUB:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a - b)

            elif op == OpCode.MUL:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a * b)

            elif op == OpCode.DIV:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.push(a / b)

            elif op == OpCode.STORE:
                # arg = nombre de variable
                nombre = str(inst.arg)
                valor = self.stack.pop()
                self.memoria[nombre] = valor

            elif op == OpCode.LOAD:
                nombre = str(inst.arg)
                if nombre not in self.memoria:
                    raise NameError(f"Variable '{nombre}' no definida")
                self.stack.push(self.memoria[nombre])

            elif op == OpCode.PRINT:
                valor = self.stack.pop()
                print(valor)

            elif op == OpCode.HALT:
                return

            else:
                raise ValueError(f"OpCode no soportado: {op}")

            self.ip += 1