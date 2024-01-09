# creating person class 
class Person():
	pass

# father class has attribute - father_name
class Father(Person):
	father_name = ""
	def father(self):
		print(self.name)

# mother class with attribute mother_name
class Mother(Person):
	mother_name = ""
	def mother(self):
		print(self.name)

# creating derived child class
class Child(Father, Mother):
	def parents(self):
		# Using super() method to access parent classes
		super().__init__()
		print("Father :", self.father_name)
		print("Mother :", self.mother_namename)

# creating child object
child = Child()
child.__init__()
child.father_name = "Atharv"
child.mother_namename = "Gauri"
child.parents()
