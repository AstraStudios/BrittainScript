import ply.lex as lex
import math

# Lord help me, for I do not know what I am doing anymore in this gumbled mess
# Proverbs 3:5-6

tokens = (
    # basic math
    'NUMBER',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    # algebra
    #'ID', # basically math variables
    'SQUAREROOT',
    'POWER',
    # trig #**convert to degrees as well**
    'SINE',
    'COSINE',
    'TANGENT',
    # inverse trig # **convert all to degrees from radians**
    # 'INVERSESINE', #asin
    # 'INVERSECOSINE', #acos
    # 'INVERSETANGENT', #atan
    # random math
    'PI',
    'LPAREN',
    'RPAREN',
    # functions
    'PRINT',
    'IF',
    'ELSEIF',
    'WHILE',
    'FOR',
    'FUNC',
    'ASSIGN',
    'VALUE',
    # func call
    'FUNC_CALL',
    'EXPRESSION'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
# assign
t_SQUAREROOT = r'sqrroot'
t_POWER = r'\^'
t_SINE = r'sin'
t_COSINE = r'cos'
t_TANGENT = r'tan'
# t_INVERSESINE = r'isin'
# t_INVERSECOSINE = r'icos'
# t_INVERSETANGENT = r'itan'
t_PI = r'pi'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PRINT = r'push'
t_IF = r'cond'
t_ELSEIF = r'elsecond'
t_WHILE = r'while'
t_FOR = r'dur' #duration
t_FUNC = r'func'
t_ASSIGN = r'[<>]'

# regular base action
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EXPRESSION(t):
    r'[a-zA-Z][a-zA-Z0-9_]*\s*\([^)]*\)'
    return t

# Regular expression for function calls # test
def t_FUNC_CALL(t):
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
    # Replace all funcs requiring arguments here
    if func_name == 'sqrroot':
        p[0] = math.sqrt(arg)
    elif func_name == 'sin':
        p[0] = math.degrees(math.sin(math.radians(arg)))  # Convert degrees to radians
    elif func_name == 'cos':
        p[0] = math.degrees(math.cos(math.radians(arg)))  # Convert degrees to radians
    elif func_name == 'tan':
        p[0] = math.degrees(math.tan(math.radians(arg)))  # Convert degrees to radians
    elif func_name == 'push':
        p[0] = print(p[3])
    #elif func_name == 'isin':
        #p[0] = math.degrees(math.asin(arg))
    #elif func_name == 'icos':
        #p[0] = math.degrees(math.acos(arg))
    #elif func_name == 'itan':
        #p[0] = math.degrees(math.atan(arg))
    else:
        # If the function name is not recognized, assign a default value to p[0]
        print("Error: Unrecognized function '{}'".format(func_name))
        p[0] = None

def t_VALUE(t):
    r'<[^>]*>'
    t.value = t.value[1:-1] # remove the < and > from the lexer
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character or syntax error at: '%s'" % t.value[0])

lexer = lex.lex()