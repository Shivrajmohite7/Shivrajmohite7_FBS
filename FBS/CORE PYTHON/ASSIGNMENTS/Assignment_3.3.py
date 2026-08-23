# Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1=float(int(input("Enter Angle_1:")))
ang2=float(int(input("Enter Angle_2:")))
ang3=float(int(input("Enter Angle_3:")))

if ang1+ang2+ang3==180 and ang1>0 and ang2>0 and ang3>0:
    print("valid triangle")
else:
    print("not valid triangle")