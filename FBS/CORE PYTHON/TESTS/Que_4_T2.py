
length=float(int(input("Length:")))
height=float(int(input("Height:")))
cost=float(int(input("Cost:")))


total_area=0

for i in range(4):
    area=length*height
    total_area=total_area+area

total_cost=total_area*cost
print(f"Total_cost is {total_cost}")


input("enter")