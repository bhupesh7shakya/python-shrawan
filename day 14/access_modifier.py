# access modifiler

class Person:
    def __init__(self, name="test",gender=123,age=123):
        self.name=name
        self._gender=gender
        self.__age=age
     
    @property   
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age
        
        
shila=Person('shila','male','13')

shila.set_age(12)
shila.age=44