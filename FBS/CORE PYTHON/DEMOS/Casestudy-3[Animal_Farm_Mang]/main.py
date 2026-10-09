
from Farm.cow import Cow
from Farm.goat import Goat
from Farm.dog import Dog


animals=[]

while True:
    print("===== ANIMAL FARM MANAGEMENT SYSTEM =====")
    print("1.COW")
    print("2.GOAT")
    print("3.DOG")
    print("4.RECORD")
    choice=int(input("Enter Choice:"))
    if choice==1:
        print("Enter Cow Details:")
        category="COW"
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        height=float(input("Enter Height:"))
        weight=float(input("Enter Weight:"))
        color=input("Enter Color:")
        milk = float(input("Enter Milk Production (liters): "))
        health = input("Enter health: ")
       
        cow=Cow("COW",name,age,height,weight,color,milk,health)
        animals.append(cow)
    
        cow.common()
        cow.sound()
        cow.show_milk


    elif choice==2:
        print("Enter Goat Details:")
        category="GOAT"
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        height=float(input("Enter Height:"))
        weight=float(input("Enter Weight:"))
        color=input("Enter Color:")
        milk = float(input("Enter Milk Production (liters): "))
        health = input("Enter health: ")
    
        goat=Goat("GOAT",name,age,height,weight,color,milk,health)
        animals.append(goat)
    
        goat.common()
        goat.sound()
        goat.show_milk
    


    elif choice==3:
       print("Enter Dog Details:")
       category="DOG"
       name=input("Enter Name:")
       age=int(input("Enter Age:"))
       height=float(input("Enter Height:"))
       weight=float(input("Enter Weight:"))
       color=input("Enter Color:")
    # milk = float(input("Enter Milk Production (liters): "))
       health = input(f'Enter health",[Press Exact ,"H" For Healthy]: ')
    
       dog=Dog(category,name,age,height,weight,color,health)
       animals.append(dog)
       dog.common()
       dog.sound()

    elif choice == 4:

       if len(animals) == 0:
           print("No animals found")

       else:
           print("\n===== ALL ANIMAL RECORDS =====")
           for animal in animals:
               animal.common()
               print("--------------------")
    else:
        print("invalid choice")





# cow=Animal("Ganga","Cow",12,4.5,450,"White")
# cow.common()
# cow.eat()
# cow.sound()

# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Casestudy/main.py"