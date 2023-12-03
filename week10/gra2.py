from gra1 import Student
Student.count = 0
f = open('scores2.csv', 'r')
f.readline()	# ignore the header
students = [ ]
for line in f:
    roll, name, maths, physics, chemistry = line.strip().split(',')
    roll, maths, physics, chemistry = int(roll), int(maths), int(physics), int(chemistry)
    students.append(Student(name, roll, maths, physics, chemistry))
f.close()
print(Student.roll)