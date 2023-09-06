from abc import ABC,abstractmethod
from .access_modifier import Person

Person().age

class Computer(ABC):
    
    def run(self,app):
        self.process(app)
    
    @abstractmethod
    def process(self,app):
        pass


class Mobile(Computer):
    
    def process(self,app):
        print(f"Mobile is running {app}")


class Laptop(Computer):
    def process(self, app):
        print(f"Latop is running {app}")
        

samsung=Mobile()
samsung.run('pubg')
samsung.run('chrome')


lenovo=Laptop()
lenovo.run('Dota')