import ply.yacc as yacc
from testlexer import tokens

def p_expression_plus(p):
    p[0] = p[1]+p[3]

def p_expression_minus(p):
    p[0] = p[1] - p[3]

def p_expression_number(p):
    p[0] = p[1]

parser = yacc.yacc

def parse(data):
    return parser.parse(data)