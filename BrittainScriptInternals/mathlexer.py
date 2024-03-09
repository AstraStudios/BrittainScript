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
    #'ASSIGN', # basically math variables
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
    'PI'
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

# regular base action
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t'

def t_error(t):
    print("Illegal character or syntax error at: '%s'" % t.value[0])

lexer = lex.lex()