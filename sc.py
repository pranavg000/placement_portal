import csv
from home.models import Branch, Student
MNC = Branch.objects.get(branchName='MNC')
CSE = Branch.objects.get(branchName='CSE')
ECE = Branch.objects.get(branchName='ECE')
EEE = Branch.objects.get(branchName='EEE')
BT = Branch.objects.get(branchName='BT')
CL = Branch.objects.get(branchName='CL')
CST = Branch.objects.get(branchName='CST')
EP = Branch.objects.get(branchName='EP')
Design = Branch.objects.get(branchName='Design')
Others = Branch.objects.get(branchName='Others')
ME = Branch.objects.get(branchName='ME')
CE = Branch.objects.get(branchName='CE')
Physics = Branch.objects.get(branchName='Physics')
Chemistry = Branch.objects.get(branchName='Chemistry')
Mathematics = Branch.objects.get(branchName='Mathematics')


dic = {
	'Mathematics and Computing' : MNC,
	'Computer Science and Engineering' : CSE,
	'Electronics and Communication Engineering' : ECE,
	'Chemical Science and Technology' : CST,
	'Engineering Physics' : EP,
	'Electronics and Electrical Engineering' : EEE,
	'Chemical Engineering' : CL,
	'Biosciences and Bioengineering' : BT,
	'Civil Engineering' : CE,
	'Mechanical Engineering' : ME,
	'Design':Design,
	'Others':Others,
    'Mathematics' : Mathematics,
    'Physics' : Physics,
    'Chemistry' : Chemistry,
}

depts = ['M.Tech', 'B.Tech', 'B.Des', 'M.Des', 'Phd', 'M.Sc']

with open('pd.csv') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=',')) 
    print(len(csv_reader))
    for row in csv_reader[1:]:
    	if row[5] == '':
    		placed = False
    	else :
    		placed = True

    	if dic.get(row[3]) :
    		branch = dic[row[3]]
    	else :
    		branch = Others


    	if row[2] in depts:
    		program = row[2]
    	else :
    		program = 'Others'
        
    	print(row[0], row[1], program, placed, branch.branchName)
    	if len(Student.objects.filter(roll = row[0])) == 0:
    		Student.objects.create(roll=row[0], name=row[1], programs = program, branch = branch, placed=placed, company=row[5], profile=row[6])
    	











