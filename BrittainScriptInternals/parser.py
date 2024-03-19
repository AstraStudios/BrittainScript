import ply.yacc as yacc
import mathlexer as mathlexer
import textlexer as textlexer
from mathlexer import tokens
from textlexer import tokens
import math as math

symbol_table = {}

# basic function for everything thats complex
#arg = p[3]
    #if isinstance(arg, str):
        #try: arg = float(arg)
        #except ValueError:
            #print("Error: Invalid arguement '{}' for function".format(arg))
            #p[0] = None
            #return

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[3]

def p_expression_times(p):
    'expression : expression MULTIPLY expression'
    if p[1] is None or p[3] is None:
        p[0] = None  # Set the result to None if any operand is None
    else:
        p[0] = p[1] * p[3]

def p_expression_squareroot(p):
    'expression : SQUAREROOT LPAREN expression RPAREN'
    arg = p[3]
    if isinstance(arg, str):
        try: arg = float(arg)
        except ValueError:
            print("Error: Invalid argument '{}' for squareroot".format)
            p[0] = None
            return
    p[0] = math.sqrt(arg)

def p_expression_power(p):
    'expression : expression POWER expression'
    arg = p[3]
    if isinstance(arg,str):
        try: arg = float(arg)
        except ValueError:
            print("Error: Invalid argument '{}' for square".format(arg))
            p[0] = None
            return
    p[0] = math.pow(p[1], arg)

def p_expression_sine(p):
    'expression : SINE LPAREN expression RPAREN'
    arg = p[3]  # Get the argument passed to the sine function
    if isinstance(arg, str):  # Check if the argument is a string
        try:
            arg = float(arg)  # Convert the string to a numerical value
        except ValueError:
            print("Error: Invalid argument '{}' for sine function".format(arg))
            p[0] = None
            return
    # Now arg should be a numerical value
    p[0] = math.degrees(math.sin(arg))
    
def p_expression_cosine(p):
    'expression : COSINE LPAREN expression RPAREN'
    arg = p[3]
    if isinstance(arg, str):
        try: arg = float(arg)
        except ValueError:
            print("Error: Invalid argument '{}' for cosine".format(arg))
            p[0] = None
            return
    p[0] = math.degrees(math.cos(arg))

def p_expression_tangent(p):
    'expression : TANGENT LPAREN expression RPAREN'
    arg = p[3]
    if isinstance(arg, str):
        try: arg = float(arg)
        except ValueError:
            print("Error: Invalid argument '{}' for tangent".format(arg))
            p[0] = None
            return
    p[0] = math.degrees(math.tan(arg))

def p_expression_pi(p):
    'expression : PI'
    p[0] = math.pi

def p_expression_func_call(p):
    '''expression : FUNC_CALL'''

# all text stuff from here on
    
def p_expression_if(p):
    'expression : IF LESS_THAN_SIGN '


def p_assignment(p):
    'assignment : ID ASSIGN VALUE'

def p_expressionfunc_call_text(p):
    '''expression : FUNC_CALL_TEXT'''

def p_error(p):
    print("Error in input")

parser = yacc.yacc()

input_text = input("test: ")
mathlexer.lexer.input(input_text)
while True:
    tok = mathlexer.lexer.token()
    if not tok:
        break
    print(tok)
result = parser.parse(input_text)
print(result)