class mobile:
    def __init__ (self,price,brand):
        self.price = price
        self.brand = brand

    def change_price(mobile):
        print(f"ID of object inside function", id(mobile))
        mobile.price = 3000

m1 = mobile(100,"Apple")
print(f"Id of drived code",id(m1))

m1.change_price()
print("price of mobile",m1.price)



