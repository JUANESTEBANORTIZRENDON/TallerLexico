
"""
lexer,0,0.py (DEMO)

Analizador léxico para  Compiladores.



Uso:
  python "lexer,0,0.py"
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from typing import List, Optional


DEMO_SOURCE = "if (x = 10) x = x + 1;"

#se define objeto token con sus atributos para almacenar la informacion de cada token encontrado en el texto fuente
@dataclass(frozen=True)
class Token:
    type: str
    lexeme: str
    line: int
    col: int

#declaracion de las expresiones regulares 
class Lexer:
    def __init__(self) -> None:
        self.keywords = {"if", "else", "while"}
        self.master_pattern = re.compile(
            r"(?P<WHITESPACE>\s+)"
            r"|(?P<IDENTIFIER>[a-z]+)"
            r"|(?P<INTEGER>[0-9]+)"
            r"|(?P<OPERATOR>[+\-*/=])"
            r"|(?P<DELIMITER>[();])"
        )

    #VALIDACION PARA AVANZAR EN EL TEXTO Y CONTAR LAS LINEAS Y COLUMNAS PARA LOS TOKENSY ORGANIZA LOS TOKENS EN UNA TABLA PARA MOSTRARLOS DE FORMA ORDENADA
    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []
        pos = 0
        line = 1
        col = 1

        while pos < len(text):
            match = self.master_pattern.match(text, pos)
            if not match:
                bad_char = text[pos]
                raise ValueError(
                    f"Error léxico: carácter inválido '{bad_char}' en línea {line}, columna {col}."
                )

            kind = match.lastgroup
            if kind is None:
                raise RuntimeError("Error interno: match sin grupo.")
            lexeme = match.group(kind)

            start_line, start_col = line, col
            line, col = self._advance_position(lexeme, line, col)

            if kind == "WHITESPACE":
                pos = match.end()
                continue

            if kind == "IDENTIFIER":
                token_type = "KEYWORD" if lexeme in self.keywords else "IDENTIFIER"
            elif kind == "INTEGER":
                token_type = "INTEGER"
            elif kind == "OPERATOR":
                token_type = "OPERATOR"
            elif kind == "DELIMITER":
                token_type = "DELIMITER"
            else:
                raise RuntimeError(f"Tipo de token inesperado: {kind}")

            tokens.append(Token(token_type, lexeme, start_line, start_col))
            pos = match.end()

        return tokens

#PERMITE SEGUIR LEENDO LA LINEA DDDE LA INSTRUCCION EN CASO DE UQE TENGA SALTOS DE LINEA 
    @staticmethod
    def _advance_position(lexeme: str, line: int, col: int) -> tuple[int, int]:
        newlines = lexeme.count("\n")
        if newlines == 0:
            return line, col + len(lexeme)

        last_newline_index = lexeme.rfind("\n")
        chars_after_last_newline = len(lexeme) - last_newline_index - 1
        return line + newlines, 1 + chars_after_last_newline

#FUNSION PARA PONER LOS TOKEN EN UNA TABLA 
def format_tokens(tokens: List[Token]) -> str:
    lines = []
    header = f"{'TYPE':<12} {'LEXEME':<10} {'LINE':<5} {'COL':<5}"
    lines.append(header)
    lines.append("-" * len(header))
    for t in tokens:
        lines.append(f"{t.type:<12} {t.lexeme:<10} {t.line:<5} {t.col:<5}")
    return "\n".join(lines)

#FUNSION PRINCIPAL  
def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if argv:
        if argv in (["-h"], ["--help"]):
            print(__doc__.strip())
            return 0
        print("Este programa está en modo demo y no acepta argumentos.")
        print('Ejecuta: python "lexer,0,0.py"')
        return 2

    source = DEMO_SOURCE
    lexer = Lexer()
    try:
        tokens = lexer.tokenize(source)
    except ValueError as e:
        print(str(e))
        return 1

    print("=== Código fuente (demo) ===")
    print(source)
    print("\n=== Tokens ===")
    print(format_tokens(tokens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
