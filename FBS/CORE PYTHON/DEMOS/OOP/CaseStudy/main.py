from empmanage import EmpManage
class Main:
    @staticmethod
    def login():
        eid=input("enter user id :")
        epass=input("enter password:")

        if eid=="Admin" and epass=="1234":
            print("Logged in ")
            return True
        else:
            print("Invalid Credentials")
    def menu(self):
       em=EmpManage()
       while True:
           print("1.Add Employee")
           print("2.Display Employee")
           print("3.Search Employee")
           print("4.Update Employee")
           print("5.Delete Employee")
           print("6.Exit Employee")
           choice=int(input("Enter Choice:"))
           if choice==1:
               print("Add")
               em.addEmp()
           elif choice==2:
               print("Display")
               em.addEmp()
           elif choice==3:
               print("Search")
               em.addEmp()
           elif choice==4:
               print("Update")
               em.addEmp()
           elif choice==5:
               print("Delete")
               em.addEmp()
           elif choice==6:
               print("THNX VISIT AGAIN PRT YA")
               break
           else:
               print("Invalid Choice")
res=Main.login()
if res:
    m=Main()
    m.menu()
    print(res)












