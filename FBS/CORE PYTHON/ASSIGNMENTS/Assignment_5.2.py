
# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

students=int(input("enter studdents:"))

for i in range(1,students+1):
    print(f"student:{i}")

    marks1=int(input("Biology :"))
    marks2=int(input("Math:"))
    marks3=int(input("Science:"))
    marks4=int(input("Marathi:"))
    marks5=int(input("English:"))
    sum=marks1+marks2+marks3+marks4+marks5

    if sum>500:
       print("invalid")
    else:
        per=sum/500*100
        print(f"percentage is {per}")

        avg=sum/5
        print(f"average is {avg}")


