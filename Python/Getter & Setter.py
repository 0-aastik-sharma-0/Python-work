class bus:
    def __init__(self,name,depot):
        self.name = name
        self.__depot = depot
    def set_depot(self,name,depot):
        self.__depot = depot
    def get_depot(self):
        return self.__depot

b1 = bus("HRTC","f")






































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
