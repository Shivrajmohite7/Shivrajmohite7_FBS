# 1. Create a class Emp (eid,ename,basic)

import pickle
class Emp:
    def __init__(self,eid,ename,basic):
        self.eid=eid
        self.ename=ename
        self.basic=basic
    def __str__(self):
        return f"Employee Id:{self.eid},Employee Name:{self.ename},Employee Basic Salary:{self.basic}"

e1=Emp(101,"Rahul",50000)
e2=Emp(102,"Mitesh",40000)
e3=Emp(103,"Mukund",60000)

f=open("C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Dat22.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
f.close()

# file="Dat22.dat"
file = "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Dat22.dat"
file_obj=open(file,'rb')

e1=pickle.load(file_obj)
e2=pickle.load(file_obj)
e3=pickle.load(file_obj)
print(e1)
print(e2)
print(e3)
# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Assignment22.1.py"