import ply.lex as lex
# math specific lexer(may merge both lexers)
tokens = (
    # basic math
    'NUMBER',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    # algebra
    'ASSIGN', # basically math variables
    # geometry
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'

# regular base action
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



t_ignore = '\t'