class bus:
    def __init__(self,name,depot):
        self.name = name
        self.__depot = depot
    def set_depot(self,name,depot):
        self.__depot = depot
    def get_depot(self):
        return self.__depot

b1 = bus("HRTC","Hamirpur")
print(b1.name,b1.get_depot())
