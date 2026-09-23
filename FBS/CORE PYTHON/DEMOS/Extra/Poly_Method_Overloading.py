
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,other):
        newreal=self.real+other.real
        newimg=self.img+other.img

        return Complex(newreal,newimg)
num1=Complex(1,3)
num1.showNum()
num2=Complex(4,5)
num2.showNum()

num3=num1+num2
num3.showNum()