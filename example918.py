from sys import argv, stderr

try:
  prog, infile, outfile, numquiz = argv
  numquiz = int(numquiz)

except:
  raise SystemExit("{0:}: Incorrect command: use {0:} '<infile> <outfile> <int>'"\
    .format(argv[0]))
  
for wd in [prog, infile, outfile, numquiz]:
  print(wd)
  
  #read the documentation for csv module
  #open the file, create a csv reader