
# task 
# create son object
# print 3 lvl constructor

class GrandFather:
    def __init__(self) -> None:
        print('i am  GrandFather')
        
    def house(self):
        print('house')
        
class Father(GrandFather):
    def __init__(self) -> None:
        print('i am  father')
        
    def car(self):
        print('bmw')
    
class Mother:
    def jewellary(self):
        print("jewllary")
        
class Son(Father,Mother):
    def __init__(self) -> None:
        print('i am  son')
        super().__init__()
        
    def ps5(self):
        print('ps5')
    
    def car(self):
        print('ferrari')
        super().car()
        

son=Son()
father=Father()


print(isinstance(son,object))
# son.ps5()
# son.car()
# son.house()
# son.jewellary()




