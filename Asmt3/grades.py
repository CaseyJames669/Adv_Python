# file: grades.py
# author: Casey Bladow
# Student grades program

'''
This script takes an input csv file from the command line and creates an
output file including average assignment scores, average quiz scores,
and exam scores as well as their final score sorted by their last name. 
'''

from sys import argv, stderr
import csv

def comLine():
  '''Grab the program name, input file, output file, and number of quizzes used
  to evaluate the quiz average from the command line.
  
  Preconditions:
    prog and infile are already created, numOfQuizzes is known
  Postconditions:
    Returns infile, outfile, and number of quizzes. If the number of command
    line arguments don't match the requirements, and error exception is
    thrown.
  '''
  # makes sure the correct number of command line arguments are entered
  try:
    prog, infile, outfile, numOfQuizzes = argv
    numOfQuizzes = int(numOfQuizzes)

  # throws an exception and kills the program is an incorrect number of 
  # command line arguments are entered.
  except:
    raise SystemExit\
      ("{0:}: Incorrect command: use {0:} '<infile> <outfile> <int>'".\
	format(argv[0]))
  
  # returns the input file, output file, and number of quizzes
  return infile, outfile, numOfQuizzes

def read_data(infile):
  '''Reads the input file and returns dictKeys, key, and students list
  
  Preconditions:
    infile is an actual csv file
  Postconditions:
    dictKeys are created for .DictReader and .DictWriter
    key line is created to figure out the points possible in each category
    students list is created
  '''
  with open(infile, 'r', newline='') as csv_in:
    csv_reader = csv.reader(csv_in, delimiter=',', quotechar='"')
    
    #reads very first line and creates dictKeys
    dictKeys = next(csv_reader)
    
    #reads the next line for a points possible list
    key = next(csv_reader)
    
    #creates students list
    students =[]
    for stu in csv_reader:
      students.append(stu)
      
    #returns dictKeys, key list, and students list
    return dictKeys, key, students

def parse_summary(key):
    '''key contains data for the points possible for assignment scores, quiz
     scores, and exam scores
    
    Preconditions:
      key is list of the points possible for each assignment, quiz, and exam
      
    Postconditions:
      returns tuple consisting of:
	list of max scores for assignments
	list of max scores for quizzes
	list of max scores for exams
    '''
    #The next 3 lines pull from the [2] list value to the first blank value
    #creating a list of all the points possible for assignments
    key_scores = [float(x) if x != '' else x for x in key [2:]]
    blank1 = key_scores.index('',)
    assignments = key_scores[:blank1]
    na = sum(assignments)
    #The next 3 lines pull from the first blank value to the second blank value
    #creating a list of all the points possible for quizzes 
    blank2 = key_scores.index('',blank1+1)
    quizzes = key_scores[blank1+1:blank2] 
    nq = sum(quizzes)
    #The next 2 lines pull from the second blank value to the end of the list
    #creating a list of all the points possible for exams
    exams = key_scores[blank2+1:]
    ne = sum(exams)
    #returns a list of points possible for assignments, quizzes, exams, and the
    #actual quizzes list 
    return na, nq, ne, quizzes

def parse_student(students, key_as, key_ex, key_qz, numOfQuizzes, quizzes):
  '''Grabs the students list, line by line, and pulls the first name
    last name, all the assigment scores and adds them up, all the
    quiz scores are actually pulled into another list for use later, and all
    the exam scores and sums them up. Finally, returning the studentTotals2 
    list for the output file.
    
    Preconditions:
      students list is properly created 
      all key objects were created properly in the parse_summary function
      comLine function also had to worked properly to get the numOfQuizzes
      
    Postconditions:
      returns studentTotals2 list that will be used to created the final output
      file.
      the list will contain name, assignment average, quiz average, exam
      average and final grade average
  '''
  #creates studentTotals list
  studentTotals = []
  for stu in students:
    #assigns name
    name = (stu[0:2])
    #flips name for lastName, firstName
    name = name[1],name[0]
    #adds up all the achieved assignment points
    stu_as = sum([0 if x == '' else float(x) for x in stu[2:15]])
    #creates the student quiz scores list, used in comp_qz_avg
    stu_qz_list = []
    stu_qz_list = stu[15:27]
    #adds up all the achieved exam points
    stu_ex = sum([0 if x == '' else float(x) for x in stu[27:32]])
    #appends name to studentTotals2 list
    studentTotals.append(name)
    
    #calls comp_as_avg, assigns it to avg_as and appends it to studentTotals2
    avg_as = comp_as_avg(stu_as, key_as)
    studentTotals.append(avg_as)
    
    #calls comp_qz_avg, assigns it to avg_qz and appends it studentTotals2
    avg_qz = comp_qz_avg(stu_qz_list, key_qz, numOfQuizzes, quizzes)
    studentTotals.append(avg_qz)
    
    #calls comp_ex_avg, assigns it to avg_ex and appends it to studentTotals2
    avg_ex = comp_ex_avg(stu_ex, key_ex)
    studentTotals.append(avg_ex)
    
    #calls comp_fin_avg, assigns it to finalScore and appends it to
    #studentTotals2 list
    finalScore = comp_fin_avg(avg_as, avg_ex, avg_qz)
    studentTotals.append(finalScore)
    
    #calls the studentTotals list, slices it every 5 entries, and creates
    #list called studentTotals2
    studentTotals2=[studentTotals[x:x+5] for x in range(0, len(studentTotals), 5)]
    studentTotals2.sort()
    
  #returns the newly created studentTotals2 list
  return studentTotals2

def comp_fin_avg(avg_as, avg_ex, avg_qz):
  '''Computes the final score
  
  Preconditions:
    assignment average, exam average, and quiz average have all been calculated
  Postconditions:
    returns the students final score
  '''
  #assignments account for 45% of final grade
  #quizzes account for 10% of final grade
  #exams account for the remaining 45% of final grade
  finalScore = (float(avg_as) * .45) + (float(avg_qz) * .10) + (float(avg_ex) * .45)
  finalScore = ("%0.2f" % finalScore)
  #returns finalScore
  return finalScore

def write_data(outfile, studentTotals):
  '''writes to the output file given in the command line arguments
  
  Preconditions:
    studentTotals2 list has been created and everything has been sent to it
  Postconditions:
    a new file is created
  '''
  with open(outfile, 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(studentTotals)

def comp_qz_avg(stu_qz_list, key_qz, numOfQuizzes, quizzes):
    '''Convert quizzes to ratios, sort them from highest to lowest,
    keep the number specified from numOfQuizzes.
    
    Preconditions:
      student quiz list is created
      points possible for quizzes is figured out
      number of quizzes used for average was properly entered
      
    Postconditions:
      Returns quiz average
    '''
    #creates a tmp list for sorting quiz percentage ratios
    qzPerc = []
    qzPerc = [float(a)/float(b) for a,b in zip(stu_qz_list, quizzes) if a != '']
    #reverses list to report the highest grade first
    qzPerc.sort(reverse = True)
    
    #Get the top scores
    #creates a tmp topScores list
    topScores = []
    x=0
    #flag error if too many quizzes are entered
    if numOfQuizzes > len(quizzes):
      print("You entered too many quizzes: All will be used.")
      numOfQuizzes = int(len(quizzes)) #ERROR HERE
    while x < numOfQuizzes:
      topScores.append(qzPerc[x])
      x+=1
    avg_qz = sum(topScores)/numOfQuizzes
    # return quiz average
    avg_qz *= 100
    avg_qz = ("%0.2f" % avg_qz)
    return avg_qz

def comp_as_avg(stu_as, key_as):
    '''Determines the average assigment score
    
    Preconditions:
      Total points gathered has been figured out
      Total points possible has been figured out
      
    Postconditions:
      Sends back the average assigment score
    '''
    avg_as = stu_as/key_as
    avg_as *= 100
    avg_as = ("%0.2f" % avg_as)
    
    # Return average assignment score
    return avg_as

def comp_ex_avg(stu_ex, key_ex):
  '''Determines the average exams score
  
  Preconditions:
    Total points gathered has been figured out
    Total points possible has been figured out
    
  Postconditions:
    Sends back the average quiz score
  '''
  avg_ex = stu_ex/key_ex
  avg_ex *= 100
  avg_ex = ("%0.2f" % avg_ex)
      
  # Return exam average
  return avg_ex
  
def main():
  ''' main program algorithm'''
  infile, outfile, numOfQuizzes = comLine()
  dictKeys, key, students = read_data(infile)
  key_as, key_qz, key_ex, quizzes = parse_summary(key)
  studentTotals2 = parse_student(students, key_as, key_ex, key_qz, numOfQuizzes, quizzes)

  #inserts heading - ALL MESSED UP
  studentTotals2.insert(0, "{}{}{}{}{}".format("Name", "HWavg", "QZavg", "EXavg", "Final"))

  write_data(outfile, studentTotals2)
  
if __name__ == "__main__": main()