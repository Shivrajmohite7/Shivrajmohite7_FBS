# Binary Search Algorithm.

# requirment:
# 1.List should be sorted means no jumbled it can be in ascending form or descending form
# 2.No duplicates allowed
# 3.Finding fast element in sorted list 


def getData(li,src_ele):
    be=0
    end=len(li)-1

    while(be<=end):
        mid=(be+end)//2

        if (src_ele==li[mid]):
            return mid
        
        elif(src_ele<li[mid]):
            end=mid-1

        elif(src_ele>li[mid]):
            be=mid+1

        else:
            return -1


li=[10,20,30,40,50]
num=int(input("enter:"))

result=getData(li,num)

if result != -1:
    print(f"{num} at {result}")
else:
    print("not present")


input("enter")