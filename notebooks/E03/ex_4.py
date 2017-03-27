from sys import argv, stderr
from os.path import basename

# Parse command line
try:
    program, infile = argv
    program = basename(program)
except:
    print("{0}: Error in command line.  Use {0}  <input_file_pathname>".format(basename(argv[0]), file=stderr)
    exit()

# Open the input file for reading
try:
    datafile = open(infile, 'r')
except IOError:
    print("{}:  Input file '{}' cannot be opened for reading".format(program, infile), file=stderr)
    exit()

# Read and process input file
data = datafile.read()
print(data)

datafile.close()
