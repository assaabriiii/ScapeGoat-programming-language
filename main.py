from lexer import Lexer 


text_input = """
Drucken(4 + 4 - 2)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for i in tokens : 
    print(i)