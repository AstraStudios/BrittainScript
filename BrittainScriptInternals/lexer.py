import ply.lex as lex
import math

# Lord help me, for I do not know what I am doing anymore in this gumbled mess
# Proverbs 3:5-6

# Define reserved keywords
reserved = {
    'cond': 'IF',
    'elsecond': 'ELSEIF',
    'while': 'WHILE',
    'dur': 'FOR',
    'push': 'PRINT',
    'var': 'VAR',
    'set': 'SET'  
}

# Define tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'SQUAREROOT',
    'POWER',
    'SINE',
    'COSINE',
    'TANGENT',
    'PI',
    'LPAREN',
    'RPAREN',
    'NAME',  
    'FUNC_CALL',
    'STRING',
) + tuple(reserved.values())

# Regular expression rules for tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='
t_SQUAREROOT = r'sqrroot'
t_POWER = r'\^'
t_SINE = r'sin'
t_COSINE = r'cos'
t_TANGENT = r'tan'
t_PI = r'pi'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t
    
def t_FUNC_CALL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)'
    t.value = t.value.split('(')
    func_name = t.value[0].strip()
    arg_str = t.value[1][:-1].strip()  # Remove parentheses from the argument string
    try:
        arg = float(arg_str)
    except ValueError:
        print(f"Error: Invalid argument '{arg_str}' for function '{func_name}'")
        t.value = None
        return t
    if func_name == 'sqrroot':
        t.value = math.sqrt(arg)
    elif func_name == 'sin':
        t.value = math.degrees(math.sin(math.radians(arg)))
    elif func_name == 'cos':
        t.value = math.degrees(math.cos(math.radians(arg)))
    elif func_name == 'tan':
        t.value = math.degrees(math.tan(math.radians(arg)))
    elif func_name == 'push':
        t.value = print(arg)
    else:
        print(f"Error: Unrecognized function '{func_name}'")
        t.value = None
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_WHITESPACE(t):
    r'\s+'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()