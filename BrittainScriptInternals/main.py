import lexer
import parser

#def detect_characters(data):
    #math_operators = {'+', '-','*','/'} # add more when i add more
    #return any(char in math_operators for char in data)

def parse_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read
        math_data = []
        text_data = []
        
        for line in file:
            if any(char in line for char in {'+','-','*','/'}):
                math_data.append(line)
            else:
                text_data.append(line)
        
        #math_lexer = 