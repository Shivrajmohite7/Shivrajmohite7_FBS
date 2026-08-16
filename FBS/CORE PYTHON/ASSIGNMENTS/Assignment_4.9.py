# 9. WAP to print all numbers in a range divisible by a given number.

num=int(input("enter number:"))
start=int(input("enter:"))
stop=int(input("enter:"))

for i in range(start,stop+1):
    if i%num==0:
        print(i)