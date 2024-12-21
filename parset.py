import sys

if __name__ == 'main':
    if len(sys.argv) != 2:
        raise SystemExit("Usage : python parset.py <filename>")
    filename = sys.argv[1]
    with open(filename) as file:
        source = file.read()
        print(source)