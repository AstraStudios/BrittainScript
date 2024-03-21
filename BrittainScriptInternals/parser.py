import ply.yacc as yacc
import lexer as lexer
from lexer import tokens
import math as math

variables = {}

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

def p_expression_print(p):
    'expression : PRINT LPAREN expression RPAREN'
    p[0] = p[3]

#def p_statement_assignment(p):
    #'statement : assignment'
    #pass

#def p_statement_expression(p):
    #'statement : expression'
    #p[0] = evaluate_expression(p[1])
    #p[0] = p[3]

def p_expression_name(p):
    'expression : NAME'
    p[0] = variables[p[1]]

def p_assignment(p):
    'expression : NAME EQUALS expression'
    print("Assigned variable ", p[1], "to ", p[3])
    variables[p[1]] = p[3]

# Define a function to evaluate expressions, replacing variable names with their values
#def evaluate_expression(expr):
    #if isinstance(expr, str) and expr in variables:
        #return variables[expr]  # If the expression is a variable, return its value
    #else:
        #return expr  # Otherwise, return the expression unchanged

def p_error(p):
    print("Error in input")

parser = yacc.yacc()

input_text = input("Test: ")
lexer.lexer.input(input_text)
while True:
    tok = lexer.lexer.token()
    if not tok:
        break
    print(tok)
result = parser.parse(input_text)
print(result)
print(variables)