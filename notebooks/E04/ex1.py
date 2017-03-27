# This line above is IPython magic ... NOT Python code.
# The "magic" causes the file to be written, containing the code below, when you execute this cell.

from sys import argv, exit
try:
    prog, infile1, infile2, outfile = argv
except ValueError:
    exit('{0}: Incorrect number of arguments.  Use: {0} <infile_1> <infile_2> <outfile>'.format(argv[0]))
    
print(prog, infile1, infile2, outfile)