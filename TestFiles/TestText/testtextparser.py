import ply.yacc as yacc
from testtextlexer import tokens

def p_statement_if(p):
    'statement : IF expression COLON statements'
    if p[2]:
        # execute as true
        print("Executing")
    else:
        print("skipping")
        # execute as false
        

def p_statement_else(p):
    'statement : ELSE expression COLON statements'

def p_expression(p):
    '''expression : expression PLUS expression
                    | expression MINUS expression
                    | NUMBER'''