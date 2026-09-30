# abstract method 
# 1.need to implement compulsary in subclass 
# 2.no body only defination



from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def stop():
        pass
class Bike(Vehicle):
    def start(self):
        print("Start Method")
    def stop(self):
        print("Stop Method")
class Car(Vehicle):
    def start(self):
        print("Start Method")
    def stop(self):
        print("Stop Method by Drum brake")

b1=Bike()
b1.start()
b1.stop()
c1=Car()
c1.start()
c1.stop()


input("enter")