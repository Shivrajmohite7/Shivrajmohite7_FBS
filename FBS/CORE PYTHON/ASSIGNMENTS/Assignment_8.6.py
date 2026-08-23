
# Write a program find reverse of a number

def reverse(num):
    rev=""
    for i in range(len(str(num))-1,-1,-1):
        rev=rev+str(num)[i]
    return rev


number=int(input("enter:"))
result=reverse(number)
print(result)
