#  Write a program to calculate area of rectangle

def Area_Rect(l,w):

    area=l*w
    return (f"area of rectangle is {area}")

len=float(input("enter length: "))
wid=float(input("enter width: "))
Rect=Area_Rect(len,wid)
print(Rect)

