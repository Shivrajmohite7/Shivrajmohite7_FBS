
# # # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# # #  determine if the input string is valid.

# # def getData(paren):
# #     slow=[]
# #     pairs={
# #         "}":"{",
# #         ")":"(",
# #         "]":"["
# #     }
# #     for i in paren:
# #         if i in "{([":
# #             slow.append(i)
# #         else:
# #             if not slow or slow.pop()!=pairs[i]:
# #                 return False
# #     return len(slow)==0

# # paren=input("enter:")
# # result=getData(paren)
# # print(result)

# # input("enter")




# # class A:
# #     def add(self):
# #         print("Add A")

# # class B:
# #     def add(self):
# #         print("Add B")

# # class C(B, A):
# #     def add(self):
# #         print("Add C")
# # c1 = C()
# # c1.add()



# class Emp():
#     def calsal(self):
#         print("emp cal sal")

# class Hr(Emp):
#     def calsal(self):
#         print("Hr cal sal")

# class Admin(Emp):
#     def calsal(self):
#         print("Admin cal sal")

# h=Hr()
# h.calsal()

# 1. additon

# class add:

#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         x=0
#         x=self.a+self.b
#         print(f"sum is {x}")
# ans1=add(2,3)
# ans1.display()


# add two string 

# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(f"{self.a} {self.b}")
# ans1=add("hellow","world")
# ans1.display()


# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(f"{self.a} {self.b}")

# ans1=add([1,2,3,4],[11,22,33])
# ans1.dsiplay()





class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid
    def display(self):
       print(f"id={self.id}\tName={self.name}\tSal={self.sal}")
    def calSal(self):
        print("Emp Sal=",{self.sal})
# Emp Ends here........................
class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com=com
    def getCom(self):
            return self.com
    def setcom(self,newcom):
            self.com=newcom
    def calSal(self):
        print(f"Fianl HR Sal= {self.com+self.getSal()}")
# Hr Ends HEre............................................
    
    
class Dev(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
            return self.com
    def setBonus(self,newbon):
            self.bonus=newbon
    def calSal(self):
        print(f"Fianl Dev Sal= {self.bonus+self.getSal()}")
# Devoloper Ends HEre............................................
    
e1=Employee(12,"Sachin",900999)
h1=Hr(18,"Smriti",85669,1000)
d=Dev(1,"Pravin",89650,100)
e1.calSal()
h1.calSal()
d.calSal()











input("Enter to exit...")
