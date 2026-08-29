# 10. Write a program to print list after removing even numbers.

def getData(li):
    i=0
    while i<len(li):
        if li[i]%2==0:
            del li[i]
        else:
            i+=1

    return li

li=[10,20,30,1,3,5,7]
result=getData(li)
print(result)
