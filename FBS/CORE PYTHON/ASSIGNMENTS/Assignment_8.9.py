# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

 
def arm(num):
    sum=0
    power = len(str(num))
    for i in str(num):
        sum +=int (i)**power
        # sum=sum+i**len(str(num))
    if sum==num:
        return "Armstrong"
    else:
        return "Not Armstrong"

abc=int(input("enter:"))
result=arm(abc)
print(result)

