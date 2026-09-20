
# element index which is duplicated

def getData(li,src_ele):

    for i in range(0,len(li)):
        if (src_ele==li[i]):
            return i
    else:
        return -1

li=[10,10,20,30,40,50,60,60,60]
num=10
result=getData(li,num)

if result!=-1:
    print(f"{num} at index {result+1}")
else:
    print("not found")