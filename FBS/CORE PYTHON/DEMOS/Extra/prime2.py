# strong number

num=int(input("enter num:"))
sum=0
for i in num:
    i = int(i)
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+fact
if sum==num:
    print("strong number")
else:
    print("not strong number")
