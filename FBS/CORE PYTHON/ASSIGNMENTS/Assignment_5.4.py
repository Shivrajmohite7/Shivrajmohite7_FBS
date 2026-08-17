# 4. WAP to print Armstrong number within a given range

num=int(input("enter number:"))
for i in range(1,num+1):
    total=0
    j = str(i)  #--string conversion
    k=len(j)    #len of string

    for l in str(j):
        l=int(l)

        total=total+l**k
    if total==i:
        print(i)
