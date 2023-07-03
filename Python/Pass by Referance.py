'''pass by Reference'''

class Mobile:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
def changed_price(mobil_obj):
    mobil_obj.price = 3000

m1=Mobile(100,"Apple")
changed_price(m1)
print(m1.price,m1.brand)
