import ply.yacc as yacc
from testlexer import tokens

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1]+p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Error in input!")

parser = yacc.yacc()

def parse(data):
    return parser.parse(data)