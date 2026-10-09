from .animals import Animal
from .deocrators import decorator
class Goat(Animal):
    def __init__(self,name,category,age, height, weight, color,milk,health):
        super().__init__(name,category,age,height,weight,color,health)
        self.milk=milk
        
        
    @decorator
    def sound(self):
        print(self.name,"says meh")
        
    def show_milk(self):
        print(self.milk,"litres")