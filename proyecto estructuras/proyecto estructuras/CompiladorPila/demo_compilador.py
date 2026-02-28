from __future__ import annotations
from typing import List

from instrucciones import Instruccion, OpCode
from maquina_pila import MaquinaPila


def compilar_ejemplo() -> List[Instruccion]:
    """
    “Compila” un mini programa a bytecode.

    Fuente (imaginaria):
        x = 2 + 3 * 4
        print(x)

    Nota: Esto no parsea texto; solo muestra la idea del compilador:
    generar instrucciones para una VM basada en pila.
    """
    programa = [
        Instruccion(OpCode.PUSH_CONST, 2),
        Instruccion(OpCode.PUSH_CONST, 3),
        Instruccion(OpCode.PUSH_CONST, 4),
        Instruccion(OpCode.MUL),              # 3*4 -> 12 en la pila
        Instruccion(OpCode.ADD),              # 2+12 -> 14
        Instruccion(OpCode.STORE, "x"),       # x = 14
        Instruccion(OpCode.LOAD, "x"),        # push x (14)
        Instruccion(OpCode.PRINT),            # imprime 14
        Instruccion(OpCode.HALT),
    ]
    return programa


def imprimir_programa(programa: List[Instruccion]) -> None:
    print("=== Bytecode generado ===")
    for i, inst in enumerate(programa):
        print(f"{i:02d}: {inst}")
    print()


def main() -> None:
    programa = compilar_ejemplo()
    imprimir_programa(programa)

    vm = MaquinaPila()
    print("=== Ejecución ===")
    vm.ejecutar(programa)

    print("\n=== Estado final (memoria) ===")
    print(vm.memoria)


if __name__ == "__main__":
    main()