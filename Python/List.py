class mobile:
    def __init__ (self,name,price):
        self.name = name
        self.price = price

mob1 = mobile("Apple",50000)
mob2 = mobile("Samsung",40000)
mob3 = mobile("INFINIX",30000)
mob4 = mobile("MI",20000)
mob5 = mobile("POCO",10000)

a_dict={
    "m1":mob1,
    "m2":mob2,
    "m3":mob3,
    "m4":mob4,
    "m5":mob5
    }

for key,value in a_dict.items():
    #if value.price > 30000:
        print(value.name,value.price)
