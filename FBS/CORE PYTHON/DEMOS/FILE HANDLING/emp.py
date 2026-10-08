class Employee:
    def __init__(self,id,sal,filed):
        self.id=id
        self.sal=sal
        self.filed=filed
        
    def display(self):
        print("EMP_ID=",{self.id})
        print("EMP_SAL=",{self.sal})
        print("EMP_FILED=",{self.filed})
    
    
emp=Employee(123,50000,"IT")
print(emp)

with open("xyz.txt", "w") as file:
    file.write(emp)

print("Employee data saved successfully!")

# f=open("xyz.txt",'w')
# # f.write("MI WON 5 CUPS \n RCB WON 2 CUPS \n")
# f.writelines(["Today is Monday","\n I am Good In Python"])
# f.close()

# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/FILE HANDLING/emp.py"