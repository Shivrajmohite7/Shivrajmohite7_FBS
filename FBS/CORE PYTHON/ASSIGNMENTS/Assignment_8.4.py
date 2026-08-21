num=int(input("enter:"))
sum=0
for i in str(num):
    i= int(i)
    fact=1
    for j in range(1,i+1):
        fact=fact*j 
    sum=sum+fact
if sum==num:
    print("strong")
else:
    print("not strong")

    