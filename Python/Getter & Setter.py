''' The methods which are meant to set a value to a private variable are called setter methods
The methods meant to access private variable values are called getter methods '''

class school:
    def __init__(self,student,id):
        self.student = student
        self.__id = id
    def set_id(self,student,id):
        self.__id = id
    def get_id(self):
        return self.__id

b1 = school("Puchku",10)
print(b1.student,b1.get_id())






































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
