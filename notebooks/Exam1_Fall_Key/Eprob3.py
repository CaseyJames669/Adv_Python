## Type your code here and then execute the cell to save your code to the Eprob3.py file
from sys import argv
try:
    prog, infile = argv
except:
    raise SystemExit("{0:}: Incorrect command line.  Use: {0:} input_file".format(argv[0]))

try:
    with open(infile) as data:
        print(data.readline())
except:
    raise SystemExit("{}: Error opening or reading file '{}'".format(prog, infile))