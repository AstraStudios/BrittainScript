import ply.lex as lex
import math as math
# math specific lexer(may merge both lexers)
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
    'INVERSESINE', #asin
    'INVERSECOSINE', #acos
    'INVERSETANGENT', #atan
    # random math
    'PI',
    'LPAREN',
    'RPAREN',
    # func call
    'FUNC_CALL'
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
t_INVERSESINE = r'isin'
t_INVERSECOSINE = r'icos'
t_INVERSETANGENT = r'itan'
t_PI = r'pi'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# regular base action
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regular expression for function calls # test
def t_FUNC_CALL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\((.*?)\)'
    t.value = t.value.split('(')
    t.value[1] = t.value[1][:-1]  # Remove the closing parenthesis
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character or syntax error at: '%s'" % t.value[0])

lexer = lex.lex()