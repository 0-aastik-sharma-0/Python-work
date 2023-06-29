'''To have a error free way of accessing and updating private variables, we create specific methods for this.

The methods which are meant to set a value to a private variable are called setter methods
The methods meant to access private variable values are called getter methods
The below code is an example of getter and setter methods:'''

class customer:
    def __init__(self,id,name,age,wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self,amount):
        self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

print("1st customer detail")
c1=customer(1,"Puchku",23,10000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
