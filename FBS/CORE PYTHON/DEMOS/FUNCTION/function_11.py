#  wap to count lowe case in string 

def getData():
    str1=input("enter:")
    count=0
    for i in str1:
        if i>="a" and i<="z":
            count=count+1
    print(count)

result=getData()