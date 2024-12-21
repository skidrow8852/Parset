import sys
from token import *
from lexer import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit("Usage : python parset.py <filename>")
    filename = sys.argv[1]
    with open(filename) as file:
        source = file.read()
        tokens = Lexer(source).tokenize()
        for token in tokens:
            print(token)