from sys import argv, stderr
import csv

def comLine():
  '''Checks that command line arguments match the proper requirements
  
  Precondition:
    User must enter the program name, the infile, and the outfile
  Postcondition:
    If all aruments are correct the program will continue running, if not
    the program will exit
  '''
  try:
    #checks to make sure the correct number of arguments are entered
    prog, infile, outfile = argv

  except:
    #Throws exception and kills program if not (see above try)
    raise SystemExit("{0:}: Incorrect command: use {0:} '<infile> <outfile>'"\
      .format(argv[0]))
  
  return infile, outfile

def read_data(fin):
  with open(fin, 'r', newline='') as csv_in:
    csv_reader = csv.reader(csv_in, delimiter=',', quotechar='"', 
			    quoting = csv.QUOTE_NONNUMERIC)
    key = next(csv_reader)
    students =[]
    for stu in csv_reader:
      students.append(stu)

    return key, student

def write_data(fout, records):
  with open(fout, 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(records)
  
def main():
  ''' main program algorithm'''
  data, records = comLine()
  read_data(data)
  
  
  #print formatted heading
  
main()

  