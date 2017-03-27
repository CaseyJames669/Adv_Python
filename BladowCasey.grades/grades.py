# file: grades.py
# author: Casey Bladow
# Student grades program

'''
This scripts takes an input file of student grades and outputs their name,
average scores, and final score. 
'''

# Opens the input and output files
inFile = open('grades.csv','r').readlines()
outFile = open('grades.grd','w')

def numOfQuizzes(data):
    '''Grabs the very first number in the input file and uses
    that as the number of quizzes reference.
    
    Preconditions:
      input file has been read
    Postconditions:
      Returns the value that states how many of the top quizzes
      will be kept
    '''
    # Determines the number of quizzes kept
    N_QZ = input()
    
    # Returns the number of quizzes that will be kept and used
    return N_QZ


def parse_summary(line):
    '''line contains data formatted with ',,' as blank coloumns,
    the points possible for assignment scores, quiz scores, and
    exam scores
    
    Preconditions:
      line contains data formatted per specifications above
      
    Postconditions:
      returns tuple consisting of:
	list of max scores for assignments
	list of max scores for quizzes
	list of max scores for exams
	all scores are numerical (float) values
    '''
    
    # splits the line into an assignments line, quiz line, and exams
    # line. Then uses the length of the list to generate key values
    # used later to evaluate the grade averages.
    key = open('grades.csv','r').readlines()[1].split(',')
    key_scores = [float(x) if x != '' else x for x in key [2:]]
    blank1 = key_scores.index('',)
    assignments = key_scores[:blank1]
    na = len(assignments)
    blank2 = key_scores.index('',blank1+1)
    quizzes = key_scores[blank1+1:blank2]
    nq = len(quizzes)
    exams = key_scores[blank2+1:]
    ne = len(exams)
    
    # returns key values 
    return na, nq, ne


def parse_student(line):
    '''Grabs the student line, line by line, and pulls the first name
    last name, all the assigment scores and adds them up, all the
    quiz scores and sums them up, and finally all the exam scores and
    adds them up
    
    Preconditions:
      line contains student data formatted per specifications above and
      must agree, in number of items, with teh lists obtained from
      parse_summary
      
    Postconditions:
      if number of items is correct, returns a four-tuple consisting of
      lists for name and assignment, quiz, and exam scores
      if number of items is incorrect, return a four-tuple consisting of
      four values of None.
    '''
    
    # grabs line, breaks it into segments, and adds those segments
    # creating the total points earned for each student in each
    # assignment, quiz, and exam
    
    ct=2
    students = open('grades.csv','r').readlines()[ct].split(',')
    for stu in students:
      name = (students[0:2])
      print(name)
      assign = sum([0 if x == '' else int(x) for x in students[2:15]])
      print(assign)
      qz = sum([0 if x == '' else int(x) for x in students[15:27]])
      print(qz)
      ex = sum([0 if x == '' else int(x) for x in students[27:32]])
      print(ex)
      studentTotals = [name, assign, qz, ex]
      students = open('grades.csv','r').readlines()[ct+1].split(',')
      ct+=1
      
    # return the values for name, assignment score, quiz score, and exam score
    return name, assign, qz, ex

def comp_qz_avg(data, key, N_QZ):
    '''Convert quizzes to ratios, sort them from highest to lowest,
    keep the number specified from N_QZ. If student quiz grade is 0, it will
    automatically be dropped.
    
    Preconditions:
      Total points gathered has been figured out
      Total points possible has been figured out
      
    Postconditions:
      Sends back the average quiz score
    '''
    qzPerc = []
    qzPerc = [float(a)/float(b) for a,b in zip(stu_qz, qz) if a != '']
    qzPerc.sort(reverse = True)
    #Get the top scores
    topScores = []
    x=0
    while x < N_QZ:
      topScores.append(qzPerc[x])
      x+=1
    avg_qz = sum(topScores)/key_qz
    # return quiz average
    return avg_qz

# Determines the average assignment score
def comp_as_avg(data, key):
    '''Determines the average assigment score
    
    Preconditions:
      Total points gathered has been figured out
      Total points possible has been figured out
      
    Postconditions:
      Sends back the average assigment score
    '''
    avg_as = stu_ex/key_ex
    # Return average assignment score
    return avg_as

# Determines the average exam score
def comp_ex_avg(data, key):
    '''Determines the average assignment score
    
    Preconditions:
      Total points gathered has been figured out
      Total points possible has been figured out
      
    Postconditions:
      Sends back the average quiz score
    '''
    avg_as = stu_ex/key_ex
    # Return exam average
    return avg_ex

def main():
  ''' main program algorithm'''
  N_QZ = numOfQuizzes(inFile)

  key_as, key_qz, key_ex = parse_summary(inFile)
  print('key_as: {}\nkey_qz: {}\nkey_ex: {}'.format(key_as, key_qz, key_ex))

  students = []
  studentTotals = []

  stu_name, stu_as, stu_qz, stu_ex = parse_student(inFile)
  print('stu_name: {}\nstu_as: {}\nstu_qz: {}\nstu_ex: {}'.format(stu_name, stu_as, stu_qz, stu_ex))

  finalList = []

  finalList.insert(0, gradestr.format('Name', 'HWavg', 'QZavg', 'EXavg', 'Final'))

  for line in inFile:
    stuData = parse_student(inFile, studentTotals)

  outFile.write('\n'.join(finalList) + '\n')

  inFile.close()
  outFile.close()

main()