
# Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

side1=float(int(input("Enter Side_1:")))
side2=float(int(input("Enter Side_2:")))
side3=float(int(input("Enter Side_3:")))

if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("valid triangle")
else:
    print("not valid triangle")
