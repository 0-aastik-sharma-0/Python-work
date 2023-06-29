class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance
        
    def update_balance(self,amount):
        self.wallet_balance += amount

    def show_balance(self):
        print(f"Your balance is {self.wallet_balance}")

print("1st customer detail")
c1=customer(1,"Puchku",23,10000)
print(c1.name,c1.age)
c1.show_balance()
