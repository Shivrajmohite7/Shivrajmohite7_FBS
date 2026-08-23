
# Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

side1=float(int(input("Enter Side 1:")))
side2=float(int(input("Enter Side 2:")))
side3=float(int(input("Enter Side 3:")))

if side1==side2==side3:
    print("equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("isocelest")
else:
    print("scalene")