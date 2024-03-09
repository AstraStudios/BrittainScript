import ply.yacc as yacc
from mathlexer import tokens
import math as math

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
    p[0] = p[1] * p[3]

def p_expression_squareroot(p):
    'expression : expression SQUAREROOT'
    p[0] = math.sqrt(p[1])

def p_expression_power(p):
    'expression : expression POWER expression'
    p[0] = math.pow(p[1], p[3])

def p_expression_sine(p):
    'expression : expression SINE'
    p[0] = math.degrees(math.sin(p[1]))
    
def p_expression_cosine(p):
    'expression : expression COSINE'
    p[0] = math.degrees(math.cos(p[1]))

def p_expression_tangent(p):
    'expression : expression TANGENT'
    p[0] = math.degrees(math.tan(p[1]))

def p_expression_inversesine(p):
    'expression : expression INVERSESINE'
    p[0] = math.degrees(math.asin(p[1]))

def p_expression_inversecos(p):
    'expression : expression INVERSECOSINE'
    p[0] = math.degrees(math.acos(p[1]))

def p_expression_inversetan(p):
    'expression : expression INVERSETANGENT'
    p[0] = math.degrees(math.atan(p[1]))

def p_expression_pi(p):
    'expression : PI'
    p[0] = math.pi

def p_error(p):
    print("Error in input")

parser = yacc.yacc()

input_text = "3 * 4 * sqrroot(16)"
result = parser.parse(input_text)
print(result)