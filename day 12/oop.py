class House:
    def __init__(self,color,garden):
        self.color=color
        self.garden=garden
    
    def __str__(self):
        return f"House color is {self.color} and land is {self.garden} acres"
    
    def __eq__(self, a) -> bool:
        return self.garden==a.garden
    
    def set_color(self,color):
        self.color=color

    def number(self,a):
        print(a)
ram_ko_ghar=House('green',10)

ram_ko_ghar.number(2)

# print(ram_ko_ghar)
# shyam_ko_ghar=House('blue',10)

# print(ram_ko_ghar.__eq__(shyam_ko_ghar))

