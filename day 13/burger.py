# using same method pizza
class Burger:

    def bun(self):
        print('bun')
        return self

    def patty(self):
        print('patty')
        return self

    def sauce(self):
        print('sauce')
        return self

    def cheese(self):
        print('cheese')
        return self
    
    def tomato(self):
        print('tomato')
        return self
    
    
ram_order=Burger()
ram_order.bun() \
            .patty() \
            .sauce() \
            .bun()