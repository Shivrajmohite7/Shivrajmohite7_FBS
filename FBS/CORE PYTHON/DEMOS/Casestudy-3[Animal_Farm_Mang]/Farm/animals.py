from .deocrators import decorator



class Animal:
    def __init__(self,name,category,age,height,weight,color,health):
        self.name=name
        self.category=category
        self.age=age
        self.height=height
        self.weight=weight
        self.color=color
        self.health=health
        
    def common(self):
        print("NAME:",self.name)
        print("CATEGORY:",self.category)
        print("AGE:",self.age)
        print("HEIGHT:",self.height)
        print("WEIGHT:",self.weight)
        print("COLOR:",self.color)
        print("HEALTH",self.health)
    @decorator
    def eat(self):
        print(self.name,"Is Eating")
        
    def sound(self):
        print(self.name,"Makes Sound")

        
# getter setter for age height weight 

def get_age(self):
    return self.age

def set_age(self,age):
    self.age=age
    
    
def get_height(self):
    return self.height

def set_height(self,height):
    self.height=height
    
    
def get_weight(self):
    return self.weight
    
def set_weight(self,weight):
    self.weight=weight
    
    