from hr import Hr
from dev import Dev
class EmpManage:
    Empdetail={}
    def addEmp(self):
        eid=int(input("Enter EmpId:"))
        if eid in EmpManage.Empdetail:
            print("Employee Already Exist")
            return 
        else:
            ename=input("Enter The EmpName=")
            esal=float(input("Enter The EmpSal="))
            print("1:Hr")
            print("2:Developer")
            
            choice=int(input("Enter Choice="))
            if choice==1:
                ecom=float(input("Enter The Commision Of Hr="))
                emp=Hr(eid,ename,esal,ecom)
            elif choice==2:
                ebon=float(input("Enter The Bonus Of Dev="))
                emp=Dev(eid,ename,esal,ebon)
            else:
                print("Invalid")
                return
            
            EmpManage.Empdetail[eid]=emp
            print("Emp Added Successfully")


        
