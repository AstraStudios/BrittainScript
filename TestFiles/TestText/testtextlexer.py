import ply.lex as lex

# testing out text

tokens = (
    'IF',
    'ELSE',
    'IDENTIFIER',
    'NUMBER'
)

t_IF = r'if'
t_ELSE = r'else'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-0_]*'
t_NUMBER = r'\d+'