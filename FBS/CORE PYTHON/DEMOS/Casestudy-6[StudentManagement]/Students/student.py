class Student:
    def __init__(self,prn,first_name,last_name,student_class,division,age,phone_number):
        self.prn=prn
        self.first_name=first_name
        self.last_name=last_name
        self.student_class=student_class
        self.division=division
        self.age=age
        self.phone_number=phone_number
        
    def display(self):
        print("PRN:",self.prn)
        print("NAME:",self.first_name,self.last_name)
        print("CLASS:",self.student_class)
        print("DIVISION:",self.division)
        print("AGE:",self.age)
        print("PHONE:",self.phone_number)
        
# student1=Student("SOE2022B0303112","JACK","TYZER",8,"B",15,7083697224)    
# student1.display()

# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Casestudy-6[StudentManagement]/Students/student.py"