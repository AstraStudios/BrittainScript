import ply.yacc as yacc
import mathlexer as mathlexer
from mathlexer import tokens
import math as math

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
    p[0] = math.sqrt(p[1])

def p_expression_power(p):
    'expression : expression POWER LPAREN expression RPAREN'
    p[0] = math.pow(p[1], p[3])

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

#def p_expression_inversesine(p):
    #'expression : INVERSESINE LPAREN expression RPAREN'
    #arg = p[3]
    #if isinstance(arg, str):
        #try: arg = float(arg)
        #except ValueError:
            #print("Error: Invalid argument '{}' for inverse sine".format(arg))
            #p[0] = None
            #return
    #if -1 <= arg <= 1:  # Check if the argument is within the valid range
        #p[0] = math.degrees(math.asin(arg))  # Convert the angle from radians to degrees
    #else:
        #print("Error: Argument '{}' is outside the valid range for inverse sine".format(arg))
        #p[0] = None

#def p_expression_inversecos(p):
    #'expression : INVERSECOSINE LPAREN expression RPAREN'
    #arg = p[3]
    #if isinstance(arg, str):
        #try: arg = float(arg)
        #except ValueError:
            #print("Error: Invalid argument '{}' for inverse cosine".format)
            #p[0] = None
            #return
    #if -1 <= arg <= 1:  # Check if the argument is within the valid range
        #p[0] = math.degrees(math.acos(arg))  # Convert the angle from radians to degrees
    #else:
        #print("Error: Argument '{}' is outside the valid range for inverse cosine".format(arg))
        #p[0] = None

#def p_expression_inversetan(p):
    #'expression : INVERSETANGENT LPAREN expression RPAREN'
    #arg = p[3]
    #if isinstance(arg, str):
        #try: arg = float(arg)
        #except ValueError:
            #print("Error: Invalid argument '{}' for inverse tangent".format)
            #p[0] = None
            #return
    #if -1 <= arg <= 1:  # Check if the argument is within the valid range
        #p[0] = math.degrees(math.atan(arg))  # Convert the angle from radians to degrees
    #else:
        #print("Error: Argument '{}' is outside the valid range for inverse tangent".format(arg))
        #p[0] = None

def p_expression_pi(p):
    'expression : PI'
    p[0] = math.pi

def p_expression_func_call(p):
    '''expression : FUNC_CALL'''

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