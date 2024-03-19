import ply.lex as lex

tokens = (
    'IF',
    'ELSEIF',
    'WHILE',
    'FOR',
    'FUNC',
    'LESS_THAN_SIGN',
    'GREATER_THAN_SIGN',
    # gonna put it here I think
    'ASSIGN',
    'VALUE',
    'FUNC_CALL_TEXT'
)

t_IF = r'cond'
t_ELSEIF = r'elsecond'
t_WHILE = r'while'
t_FOR = r'dur' #duration
t_FUNC = r'func'
t_LESS_THAN_SIGN = r'\<'
t_GREATER_THAN_SIGN = r'\>'
t_ASSIGN = r'[<>]'

# copied over from mathlexer but changed to fit text
def t_FUNC_CALL_TEXT(t):
    '''expression : FUNC_CALL'''
    # p[1] is a list containing function name and its arguments
    func_name = p[1][0]
    arg_str = p[1][1]  # The argument is a string
    try:
        # Try converting the argument to a numerical value
        arg = float(arg_str)
    except ValueError:
        # If conversion fails, print an error message and return None
        print("Error: Invalid argument '{}' for function '{}'".format(arg_str, func_name))
        p[0] = None
        return
    #if func_name == 'cond':
        #p[0] = 

def t_VALUE(t):
    r'<[^>]*>'
    t.value = t.value[1:-1] # remove the < and > from the lexer
    return t



lexer = lex.lex()