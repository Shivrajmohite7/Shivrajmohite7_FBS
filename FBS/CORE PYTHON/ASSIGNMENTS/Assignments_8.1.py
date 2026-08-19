
# 2. Write a program to calculate area of circle

def Area_Circle(area):
    area=3.14*radius*radius
    return (f"Area of Circle is {area}")


radius=float(input("Enter Radius:"))
circle=Area_Circle(radius)
print(circle)
