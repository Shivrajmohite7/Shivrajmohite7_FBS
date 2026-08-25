# simple intrest p*r*t/100

# si=lambda p,r,t:p*r*t/100
# result=si(1000,3,4)
# print(result)

# sq=[10,20,3,2,4,5]
# res=list(map(lambda num:num*num,sq))
# print(res)



# map means to perform multiple tasks on multiple iterables

def eo(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
# map:applies specific function to every iterable in list tuple
data=[1,2,3,5] 
result=list(map(lambda num:num%2==0,data))
print(result)

# filter: considers input
data=[1,2,3,4,53,4,3,4]
result=list(filter(lambda num:num%2==0,data))
print(result)

# reduce:to get one output from multiple values
from functools import reduce
data=[10,20,30,40]
result=reduce (lambda num1,num2:num1+num2,data)
print(result)
input("enter")