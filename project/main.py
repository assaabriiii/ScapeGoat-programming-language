from packages.lexer import Lexer 
from packages.parser_1 import Parser


text_input = """
Drucken(4 + 4);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()