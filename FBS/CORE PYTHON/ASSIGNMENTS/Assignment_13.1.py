# 1. Python Program to Add a Key-Value Pair to the Dictionary
dic={7:"Ronaldo",10:"messi"}
while True:
    key=int(input("enter key:"))
    value=input("enter value:")
    dic[key]=value
    inp=int(input("do you want to continue if yes press 1:"))
    if inp != 1:
        break
print(dic)