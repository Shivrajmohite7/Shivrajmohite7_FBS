# method overriding

class vehicle:
    def __init__(self,wheels):
        self.__wheels=wheels
    
    def getwheels(self):
        return self.__wheels
    def setwheels(self,wheels):
        self.__wheels=wheels
    def __str__(self):
        return(f"{self.getwheels()}")
    
class rickshaw(vehicle):
    def __init__(self, wheels,color):
        super().__init__(wheels)
        self.__color=color
        
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color
    
    def __str__(self):
        return(f"{self.getcolor()} {self.getwheels()}")
            
            
x=rickshaw(3,"white")
print(x)

x=vehicle(4)
print(x)
