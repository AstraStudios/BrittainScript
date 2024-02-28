import testtextlexer
import testtextparser

def parse_text_input(input_text):
    testtextlexer.lexer.input(input_text)
    tokens = []
    while True:
        tok = testtextlexer.lexer.token()
        if not tok:
            break
        print(tok)
        tokens.append(tok)
    result = testtextparser.parser.parse(input_text)
    return result

input_text = input("Enter a string: ")
result = parse_text_input(input_text)
print(result)