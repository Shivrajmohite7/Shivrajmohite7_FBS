
# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

Sub1 = int(input("Enter Marks Of Subject_1: "))
Sub2 = int(input("Enter Marks Of Subject_2: "))
Sub3 = int(input("Enter Marks Of Subject_3: "))
Sub4 = int(input("Enter Marks Of Subject_4: "))
Sub5 = int(input("Enter Marks Of Subject_5: "))

Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5

if Sub1 > 100 or Sub2 > 100 or Sub3 > 100 or Sub4 > 100 or Sub5 > 100:
    print("Invalid marks! Marks should be 100 or less.")
elif Total >= 460:
    print("FIRST CLASS")
elif Total >= 450:
    print("SECOND CLASS")
elif Total >= 250:
    print("PASS")
else:
    print("FAIL")