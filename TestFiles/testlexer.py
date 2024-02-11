import ply.lex as lex

# make a basic calculator to test testlexer.py and testparser.py
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_IGNORE = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex