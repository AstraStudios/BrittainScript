import ply.lex as lex

# make a basic calculator to test testlexer.py and testparser.py
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS'
)

t_PLUS = r'\+'
t_MINUS = r'\-'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

print("Initiliazed lexer")

lexer = lex.lex()