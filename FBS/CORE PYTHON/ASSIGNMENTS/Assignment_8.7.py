# 7. Write a program to find sum of digits of a number.

def getData(n):
    sum=0
    for i in str(n):
        i=int(i)
        sum=sum+i
    return (f"Sum of Digits = {sum}")

num=int(input("enter:"))
result=getData(num)
print(result)

