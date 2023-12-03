class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
    
    def display(self):
        print('name = {} roll = {} maths = {} physics = {} chemistry = {}'.format(self.name, self.roll, self.maths, self.physics, self.chemistry))

class Group:
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)