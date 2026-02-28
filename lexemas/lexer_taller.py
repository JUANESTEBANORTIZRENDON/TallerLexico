
"""
lexer_taller.py
Analizador léxico (scanner) básico para el taller de Compiladores.

Lenguaje del taller (según enunciado):
- Palabras reservadas: if, else, while
- Identificadores: letras minúsculas (a..z)+
- Números enteros: (0..9)+
- Operadores: + - * / =
- Delimitadores: ( ) ;

¿Qué hace este programa?
- Lee un código fuente (string o archivo).
- Recorre el texto de izquierda a derecha.
- Reconoce lexemas con expresiones regulares.
- Devuelve una lista de tokens con:
    * tipo (KEYWORD, IDENTIFIER, INTEGER, OPERATOR, DELIMITER)
    * lexema (el texto exacto)
    * línea y columna donde inicia el token (para reportes y depuración)

Cómo ejecutarlo (ejemplos):
1) Con texto directo:
   python lexer_taller.py --text "if (x = 10) x = x + 1;"

2) Con archivo:
   python lexer_taller.py --file programa.txt

3) Ejecutar el ejemplo integrado:
   python lexer_taller.py --demo
"""
#permite usar anotaciones de tipo con clases que aún no están definidas (Token en Lexer)
from __future__ import annotations
#provee analizador de argumentos para CLI, útil para recibir texto o archivos
import argparse
#permite leer expresiones regulares y definir estructuras de datos con @dataclass
import re
from dataclasses import dataclass
from typing import List, Optional


# =========================================================
# 1) Estructuras de datos: Token
# =========================================================

@dataclass(frozen=True)
class Token:
    """
    Representa un token resultante del análisis léxico.

    Atributos:
    - type: categoría del token (KEYWORD, IDENTIFIER, INTEGER, OPERATOR, DELIMITER)
    - lexeme: el lexema exacto leído del código fuente (por ejemplo: "if", "x", "10", "+", "(")
    - line: número de línea (inicia en 1)
    - col: número de columna (inicia en 1)
    """
    type: str
    lexeme: str
    line: int
    col: int


# =========================================================
# 2) Lexer: reglas y proceso de tokenización
# =========================================================

class Lexer:
    """
    Implementa un analizador léxico para el lenguaje del taller.

    Idea central:
    - Definimos patrones (regex) para:
        * espacios en blanco (se ignoran)
        * identificadores (solo minúsculas)
        * enteros
        * operadores
        * delimitadores
    - Si reconocemos un IDENTIFIER, verificamos si el lexema coincide
      con una palabra reservada (if/else/while). Si coincide, lo etiquetamos como KEYWORD.

    Nota sobre orden y ambigüedades:
    - IDENTIFIER reconoce "if", "else", "while" también.
    - Por eso, después de reconocer el lexema, revisamos si está en `keywords`.
      (Otra opción sería crear una regla regex aparte para keywords con prioridad,
      pero este enfoque es clásico y simple.)
    """

    def __init__(self) -> None:
        # Palabras reservadas del lenguaje
        self.keywords = {"if", "else", "while"}

        # Regex compuesta con grupos nombrados:
        # - Usamos match(...) desde la posición actual (no search), para forzar
        #   que SIEMPRE reconozca el token que comienza justo en "pos".
        #
        # Importante:
        # - [a-z]+ asegura que el identificador sea SOLO minúsculas.
        # - [0-9]+ reconoce enteros.
        # - [+\\-*/=] reconoce operadores (se escapa '-' para no crear rangos).
        # - [();] reconoce delimitadores.
        self.master_pattern = re.compile(
            r"(?P<WHITESPACE>\s+)"
            r"|(?P<IDENTIFIER>[a-z]+)"
            r"|(?P<INTEGER>[0-9]+)"
            r"|(?P<OPERATOR>[+\-*/=])"
            r"|(?P<DELIMITER>[();])"
        )

    def tokenize(self, text: str) -> List[Token]:
        """
        Convierte el texto de entrada en una lista de tokens.

        Recorre el string con un puntero `pos`.
        - Si encuentra WHITESPACE: lo ignora pero actualiza línea/columna.
        - Si encuentra IDENTIFIER: revisa si es keyword.
        - Si encuentra algo inválido: lanza ValueError con posición.

        Retorna:
            List[Token]
        """
        tokens: List[Token] = []

        pos = 0
        line = 1
        col = 1

        while pos < len(text):
            match = self.master_pattern.match(text, pos)

            if not match:
                # Carácter no reconocido por ninguna regla
                bad_char = text[pos]
                raise ValueError(
                    f"Error léxico: carácter inválido '{bad_char}' en línea {line}, columna {col}."
                )

            kind = match.lastgroup  # nombre del grupo que coincidió
            lexeme = match.group(kind)

            # Guardamos dónde inicia este lexema (antes de actualizar col/line)
            start_line, start_col = line, col

            # Actualizamos line/col según lo consumido
            # (esto sirve para reportar posiciones correctas)
            line, col = self._advance_position(lexeme, line, col)

            if kind == "WHITESPACE":
                # No producimos token, solo ignoramos espacios
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
                # No debería pasar, porque solo hay esos grupos
                raise RuntimeError(f"Tipo de token inesperado: {kind}")

            tokens.append(Token(token_type, lexeme, start_line, start_col))
            pos = match.end()

        return tokens

    @staticmethod
    def _advance_position(lexeme: str, line: int, col: int) -> tuple[int, int]:
        """
        Actualiza (line, col) después de consumir un lexema.

        - Si el lexema contiene saltos de línea, se incrementa line y se reinicia col.
        - Si no, solo avanzamos col según la longitud consumida.
        """
        # Contamos cuántos '\n' aparecen
        newlines = lexeme.count("\n")
        if newlines == 0:
            return line, col + len(lexeme)

        # Si hay saltos de línea:
        # - line aumenta en el número de saltos
        # - col será la longitud después del último '\n'
        last_newline_index = lexeme.rfind("\n")
        chars_after_last_newline = len(lexeme) - last_newline_index - 1
        return line + newlines, 1 + chars_after_last_newline


# =========================================================
# 3) Utilidades: imprimir tokens bonito
# =========================================================

def format_tokens(tokens: List[Token]) -> str:
    """
    Devuelve un string en formato tabla simple para imprimir tokens.
    """
    lines = []
    header = f"{'TYPE':<12} {'LEXEME':<10}"
    lines.append(header)
    lines.append("-" * len(header))
    for t in tokens:
        lines.append(f"{t.type:<12} {t.lexeme:<10}")
    return "\n".join(lines)


# =========================================================
# 4) CLI: ejecutar desde consola con --text / --file / --demo
# =========================================================

def read_file(path: str) -> str:
    """
    Lee un archivo de texto en UTF-8 y lo retorna como string.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_arg_parser() -> argparse.ArgumentParser:
    """
    Crea el parser de argumentos para ejecución por consola.
    """
    parser = argparse.ArgumentParser(
        description="Analizador léxico básico (taller de Compiladores)."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Código fuente como texto directo.")
    group.add_argument("--file", type=str, help="Ruta de archivo con código fuente.")
    group.add_argument("--demo", action="store_true", help="Ejecuta el ejemplo del taller.")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    Punto de entrada del programa.
    Retorna un código de salida (0 ok, 1 error).
    """
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    # 1) Selección de entrada
    source: str
    if args.demo is True:
        source = "if (x = 10) x = x + 1;"
    elif args.text is not None:
        source = args.text
    else:
        source = read_file(args.file)

    # 2) Tokenización
    lexer = Lexer()
    tokens: List[Token]
    try:
        tokens = lexer.tokenize(source)
    except ValueError as error:
        print(str(error))
        return 1

    # 3) Mostrar resultados (la tabla no imprime LINE/COL,
    #    pero el lexer sí las calcula para reportar errores)
    print("=== Código fuente ===")
    print(source)
    print("\n=== Tokens ===")
    print(format_tokens(tokens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
