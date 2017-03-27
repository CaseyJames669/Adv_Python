def read_data(fin):
    '''Read class data from a file opened for reading
    
    Purpose:
      Tell your 'story' here
    Preconditions: 
      fin is an input file, open for reading that must adhere
	to data input specs
    Postconditions:
      Returns a tuple including
	the integer number of quizzes to consider in average
	the list of key scores as a string
	the list of student records as strings	
    '''
    numq = int(fin.readline())
    key = fin.readline()
    students = []
    stu = fin.readlines()
    return numq, key, students

def comline(args):
    import sys
    infile = open
    outfile = 
    prog, infile, outfile = args

if __name__ == '__main__':
  
    if input("Test read_data? [Y/N]") in ['Y', 'y']:
      numq, key, stus = read_data()
 
      print(numq)
      print(key)
      for stu in stus:
	  print(stu)