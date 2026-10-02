from Students.student import Student

students=[]

while True:
    # print("____________________________")
    print("======Student Management=====")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==============================")
    choice=int(input("Enter Choice:"))
    if choice==1:
        prn=input("Enter PRN:")
        first_name=input("Enter First_Name:")
        last_name=input("Enter Last_Name:")
        student_class=input("Enter Student_Class:")
        division=input("Enter Division:")
        age=int(input("Enter Age:"))
        phone_number=int(input("Enter Phone:"))
        student1=Student(prn,first_name,last_name,student_class,division,age,phone_number)
        students.append(student1)
        print("=====Added Successfully=====")
        print("____________________________")
        
    elif choice==2:
        if len(students)==0:
            print("not present")
        else:
            print("=====Diplayed In Process=====")
            for i in students:
                i.display()
            print("=====Diplayed Successfully=====")
            
    
    
    elif choice==3:
        print("=====Searching In Process=====")
        ser_by_prn=input("Enter PRN:")
        for i in students:
            if i.prn==ser_by_prn:
                i.display()
                print("=====Searched Successfully=====")
                break
            else:
                print("not valid")
                
    elif choice==4:
        print("=====Updation In Process=====")
        upd_by_prn=input("Enter PRN:")
        for i in students:
            if i.prn==upd_by_prn:
                print("1.FirstName")
                print("2.LastName")
                print("3.Class")
                print("4.Divsion")
                print("5.Age")
                print("6.Phone")
                print("7.Complete Update")

                up_choice=int(input("enter choice:"))
                if up_choice==1:
                    i.first_name=input("Enter First Name:")
                elif up_choice==2:
                    i.last_name=input("Enter Last Name")
                elif up_choice==3:
                    i.student_class=int(input("Enter Class:"))
                elif up_choice==4:
                    i.division=input("Enter Division:")
                elif up_choice==5:
                    i.age=int(input("Enter Age:"))
                elif up_choice==6:
                    i.phone_number=int(input("Enter Phone Number:"))
                elif up_choice==7:
                    i.first_name = input("Enter new first name: ")
                    i.last_name = input("Enter new last name: ")
                    i.student_class = input("Enter new class: ")
                    i.division = input("Enter new division: ")
                    i.age = int(input("Enter new age: "))
                    i.phone_number = int(input("Enter new phone: "))
                    print("=====Updated Successfully=====")
                    
                else:
                    print("Invalid Choice")
                    break
                print("Student Updated Successfully")
                break

        if upd_by_prn!=i.prn:
            print("Invalid PRN")

    elif choice==5:
        print("=====Deletion In Process=====")
        
        del_prn=(input("Enter PRN To Delete:"))
        for i in students:
            if i.prn==del_prn:
                students.remove(i)
                print("DELETED SUCCESSFULLY")
                print("=====Deleted Successfully=====")
   
                break
        if del_prn!=i.prn:
            print("invalid choice")
           
    elif choice==6:
        print("Thank You")
        break
    else:
        print("Option Not Available")



# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Casestudy-6[StudentManagement]/Students/main.py"

# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Casestudy-6[StudentManagement]/main.py"
