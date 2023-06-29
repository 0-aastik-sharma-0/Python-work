class school:
    def __init__(self,student,class):
        self.student = student
        self.__class = class
    def set_class(self,student,class):
        self.__class = class
    def get_class(self):
        return self.__class

b1 = school("Puchku",10)






































'''# Defining class Car
class Car:

	# Defining method init method with a parameter
	def __init__(self, carname):
		self.__carname = carname

	# Defining Mutator Method
	def set_carname(self, carname):
		self.__carname = carname

	# Defining Accessor Method
	def get_carname(self):
		return self.__carname
# Creating an object
myCar = Car('Ford');

# Accesses the value of the variable
# using Accessor method and then
# prints it
print (myCar.get_carname())

# Modifying the value of the variable
# using Mutator method
myCar.set_carname('Porche')

# Prints the modified value
print (myCar.get_carname())
'''
