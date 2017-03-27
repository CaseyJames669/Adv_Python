# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Some data for our tests
csv_data = [
'"name1","name2","a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12",,"q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12",,"e1","e2","e3","e4"',
'"possible","possible",25,25,25,15,25,10,50,50,20,40,60,50,,10,10,10,10,10,10,10,10,10,10,10,10,,100,100,100,100',
'"Barney","Miller",25,25,25,13,22,0,50,21,5,18,0,0,,6,6,2,10,0,5,8,0,0,0,0,0,,68,55,45,56',
'"Robert","Johnson",25,25,25,0,25,0,50,26,0,31,57,16,,6,4,6,10,0,3,8,8,6,10,6,10,,66,69,91,75',
'"Bonnie","Raitt",25,25,25,12,25,10,50,46,20,35,43,35,,9,6,0,10,2,7,6,0,0,4,0,10,,87,85,74,82']

# <codecell>

# This just shows that the DictReader can process an iterable and lets us look at the dicts formed

import csv

csv_reader = csv.DictReader(csv_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
key = next(csv_reader)
students = list(csv_reader)
print(key)
print(students)

# <codecell>

# We only need one parse function, now, because all records work the same

def parse_record(record):
    name = '{}, {}'.format(record['name2'], record['name1'])
    asmt = [val for key, val in record.items() if key.startswith('a')]
    quiz =  [val for key, val in record.items() if key.startswith('q')]
    exam = [val for key, val in record.items() if key.startswith('e')]
    return name, asmt, quiz, exam

# <codecell>

# See if the key grades got parsed correctly

key_name, key_asmt, key_quiz, key_exam = parse_record(key)
print('Key:\nAsmts:', key_asmt, '\nQuizzes:', key_quiz,
       '\nExams', key_exam)

# <codecell>

# Demonstrate that the student grades are all parsed correctly
# Check this against the previous output

for stu in students:
    stu_name, stu_asmt, stu_quiz, stu_exam = parse_record(stu)
    print(stu_name,':\nAsmts:', stu_asmt, '\nQuizzes:', stu_quiz,
       '\nExams', stu_exam, '\n')

# <codecell>

# These are the computation functions for averages

def comp_asmt_avg(key_asmt, stu_asmt):
    return sum(stu_asmt) / sum(key_asmt)

def comp_quiz_avg(key_quiz, stu_asmt, num_quiz):
    ord_scores = sorted([sq / kq for sq, kq in zip(stu_quiz, key_quiz)], reverse = True)
    print("comp_quiz_avg:", ord_scores)
    return sum(ord_scores[:num_quiz]) / num_quiz

def comp_exam_avg(key_exam, stu_exam):
    ord_scores = sorted([sq / kq for sq, kq in zip(stu_exam, key_exam)], reverse = True)
    print("comp_exam_avg:", ord_scores)
    return sum(ord_scores[:-1]) / (len(key_exam) - 1)

# <codecell>

# Demonstrate how grade computations can be invoked and verify results

for stu in students:
    stu_name, stu_asmt, stu_quiz, stu_exam = parse_record(stu)
    print(stu_name)
    asmt_avg = comp_asmt_avg(key_asmt, stu_asmt)
    quiz_avg = comp_quiz_avg(key_quiz, stu_quiz, 8)
    exam_avg = comp_exam_avg(key_exam, stu_exam)
    print(asmt_avg, quiz_avg, exam_avg)

# <codecell>

# The function for computing final grade

def comp_fin_grade(ag, qg, eg):
    return 0.45 * ag + 0.1 * qg + 0.45 * eg

# <codecell>

# Computation loop over list of students

headings = ['Name', 'Asmt Avg', 'Quiz Avg', 'Exam Avg', 'Final']
stus_out = []
for stu in students:
    stu_name, stu_asmt, stu_quiz, stu_exam = parse_record(stu)
    asmt_avg = comp_asmt_avg(key_asmt, stu_asmt)
    quiz_avg= comp_quiz_avg(key_quiz, stu_quiz, 8)
    exam_avg = comp_exam_avg(key_exam, stu_exam)
    fin_avg = comp_fin_grade(asmt_avg, quiz_avg, exam_avg)
    values = [stu_name, asmt_avg, quiz_avg, exam_avg, fin_avg]
    
    stu_rec = {key : val for key, val in zip(headings, values)}
    print(stu_rec)
    stus_out.append(stu_rec)

# <codecell>

# This orders the list of students alphabetically by the contents of the 'Name' value

import operator

stus_out.sort(key= operator.itemgetter('Name'))
print(stus_out)

# <codecell>

# Now, write to a csv file

with open('test.out', 'w', newline='') as csv_out:
    csv_writer = csv.DictWriter(csv_out, headings, delimiter=',',\
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writeheader()
    csv_writer.writerows(stus_out)

# <codecell>

# Look at the output file
!cat test.out



