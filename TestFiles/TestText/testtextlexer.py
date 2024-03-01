import ply.lex as lex

# testing out text

tokens = (
    'TEXT',
)

#t_IF = r'if'
#t_ELSE = r'else'
#t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-0_]*'

def t_TEXT(t): # old name newline
    r'.+'
    return t
    #r'\n+'
    #t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character inputed '%s'" % t.value[0])
    t.lexer.skip(1)

print("Loaded lexer")

lexer = lex.lex()