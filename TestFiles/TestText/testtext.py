import testtextlexer
import testtextparser

lexer = testtextlexer.lexer

def parse_input(input_text):
    lexer.input(input_text)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok: break
        tokens.append(tok)
        print(tok)
    result = testtextparser.parser.parse(input_text)
    return result

input_text = input("Enter some text: ")
result = parse_input(input_text)
print("Parsed:", result)