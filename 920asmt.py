# file: 920asmt.py
# author: Casey Bladow
# Asmt 2

'''
Located in the ~walker/c153/fall_13/asmt2 is a file named grades2_fall.ods.

Get a copy of the file
Open it with Open Office Calc
Note that it has the format of the grade file that was specified in Asmt 1 ... 
now with all the "missed" grades filled in with zeros.
Save the file as a .csv file (making sure that the field separator is a ','
Using the technique we employed to get the file names from the command line, 
do the following:
rewrite the function to get the 'words' from the command line with the command
line like:
python33 grades.py grades2_fall.csv grades_out.csv
(i.e. just an input and output file NAME specified ... no number)
Your function should just return the file names if the correct number of them 
are there and should complain and exit if the command line is incorrect.
READ THE PYTHON DOCUMENTATION ON THE CSV MODULE ... especially on csv.reader 
and csv.writer. LOOK CLOSELY AT THE EXAMPLES!!!
write the function read_data which 
does not use try/except at this point ... so you can see what exceptions are 
raised if there is a problem,
takes one parameter (the name of the input file), 
opens the input file and creates a csv.reader object, 
reads the contents of the file into a list (notice that each line is now a 
list of fields, so you will now have a list of lists ... with the first one 
being the 'key scores' list), and 
returns the list you have created.
test both functions by specifying a valid command line to your function and 
reading the contents of the .csv file. Finally, print out, on the standard 
output, the list that is returned to the testing code by the function.
Write a function, similar to the reader, that 
takes the list you have created as a parameter,
creates a csv.writer object, and 
writes the list to the output file as a .csv file.
TEST
Submit your script using the controls below. You submit nothing ... that's the score you get.
'''

from sys import argv, stderr
import csv

def read_data(infile):
  '''Open grades2_fall.csv file, read the file, and create a list of lists.
  
  Precondition:
    file grades2_fall.csv exists and is properly formatted
    
  Postcondition:
    calls write_data function 
  '''
  
  with open(infile, newline='') as f:
    csv_reader = csv.reader(f, delimiter = ',', , quotechar='"')
    key = next(csv_reader) #added in class
    students = [] #added in class
    for stu in csv_reader: #added in class
      students.append(stu)#added in class
      #calls write_data() function
      write_data(reader)
      #print 'points possible row'
      print(row)

def write_data(reader):
  '''Write lists to grades_out.csv file
  
  Precondition:
    grades2_fall.csv has been opened and properly processed
  Postcondition:
    grades_out.csv was created and lists were properly laid out
  '''
  #opens/creates file
  with open('grades_out.csv', 'w', newline='') as i:
    writer = csv.writer(i)
    #writes each list individually 
    writer.writerows(reader)
   
def inClassExample():
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
  
def main():
  ''' main program algorithm'''
  infile, outfile = inClassExample()
  read_data(infile)
  
main()