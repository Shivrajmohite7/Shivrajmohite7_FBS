# 12.WAP to check number is armstrong or not

num=int(input("enter number:"))
sum=0

for i in str(num):
    i=int(i)
    sum=sum+i**len(str(num))
if sum==num:
    print("it is armstrong")
else:
    print("it is not an arsmtrong")