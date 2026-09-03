# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String


txt=input("enter string:")
ind=int(input("enter index:"))

result=txt[:ind]+txt[ind+1:]
print(result)
