from sys import argv
print(len(argv), "words appear on the command line")
for i, word in enumerate(argv):
    print("argv[{:d}] = {:s}".format(i, word))
