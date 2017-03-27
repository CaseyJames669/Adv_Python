# Exercise 5
from sys import argv, exit
argc = len(argv)
prog = argv[0]
if argc != 3:
    exit("{0:s}: incorrect number of arguments, use '{0:s} <input file> <output file>'".format(prog))

# Exercise 6
with open(argv[1], 'r') as infile:
    contents = infile.read()
with open(argv[2], 'w') as outfile:
    outfile.write(contents.upper())
