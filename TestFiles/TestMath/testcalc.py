import testlexer
import testparser

def parse_input(input_text):
    #input_string = ' '.join(str(tok.value) for tok in input_text)
    #testlexer.lexer.input(input_text)
    testlexer.lexer.input(input_text)
    tokens = []
    while True:
        tok = testlexer.lexer.token()
        if not tok:
            break
        print(tok)
        tokens.append(tok)
    #result = testparser.parse(tokens)
    result = testparser.parse(input_text)
    return result

input_text = input("Test: ")
result = parse_input(input_text)
print("Yacc parsed: ", result)