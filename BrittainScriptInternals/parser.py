import ply.yacc as yacc
import mathlexer as mathlexer
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
    'expression : SQUAREROOT LPAREN expression RPAREN'
    p[0] = math.sqrt(p[1])

def p_expression_power(p):
    'expression : expression POWER LPAREN expression RPAREN'
    p[0] = math.pow(p[1], p[3])

def p_expression_sine(p):
    'expression : SINE LPAREN expression RPAREN'
    p[0] = math.degrees(math.sin(p[1]))
    
def p_expression_cosine(p):
    'expression : COSINE LPAREN expression RPAREN'
    p[0] = math.degrees(math.cos(p[1]))

def p_expression_tangent(p):
    'expression : TANGENT LPAREN expression RPAREN'
    p[0] = math.degrees(math.tan(p[1]))

def p_expression_inversesine(p):
    'expression : INVERSESINE LPAREN expression RPAREN'
    p[0] = math.degrees(math.asin(p[1]))

def p_expression_inversecos(p):
    'expression : INVERSECOSINE LPAREN expression RPAREN'
    p[0] = math.degrees(math.acos(p[1]))

def p_expression_inversetan(p):
    'expression : INVERSETANGENT LPAREN expression RPAREN'
    p[0] = math.degrees(math.atan(p[1]))

def p_expression_pi(p):
    'expression : PI'
    p[0] = math.pi

def p_expression_func_call(p):
    '''expression : FUNC_CALL'''

def p_error(p):
    print("Error in input")

parser = yacc.yacc()

input_text = "4 + 6 * sin(16)"
mathlexer.lexer.input(input_text)
while True:
    tok = mathlexer.lexer.token()
    if not tok:
        break
    print(tok)
result = parser.parse(input_text)
print(result)