from .animals import Animal
from .deocrators import decorator
class Dog(Animal):
    def __init__(self,name,category,age, height, weight, color,health):
            super().__init__(name,category,age,height,weight,color,health) 
            
    @decorator
    def sound(self):
        print(self.name,"says bhow")
 