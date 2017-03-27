
# Test with a variety of values ... but best to keep it <= 8, since we're not doing anything about errors.
N_QZ = 4
# Construct your function definition, here
stu_qz = ['11', '12.3', '13', '14', '15', '', '17', '18']
qz = ['15','15','15','15','20','20','20','20']
print(stu_qz)
print(qz)

#Convert quizes to percentages
#IF stu_qz = 0 grade is automatically dropped
qzPerc = []
qzPerc = [float(a)/float(b) for a,b in zip(stu_qz, qz) if a != '']
qzPerc.sort(reverse = True)
print(qzPerc)

#Get the top scores
topScores = []
x=0
while x < N_QZ:
    topScores.append(qzPerc[x])
    x+=1
print(topScores)
