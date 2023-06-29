class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
        
    def update_balance(self,amount):
        self.__wallet_balance += amount

    def show_balance(self):
        print(f"Your balance is {self.__wallet_balance}")

print("1st customer detail")
c1=customer(1,"Puchku",23,10000)
c1.customer__wallet_balance = 5000
c1.show_balance()
