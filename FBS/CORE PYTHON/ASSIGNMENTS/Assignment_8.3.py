# 3. Write a function to find the second largest number in a list without using max().

def getData(n):
    max=n[0]
    min=n[0]

    for i in range(1,len(n)):
        if n[i]>max:
            min=max
            max=n[i]
    return min

num=[10,20,30,405]
result=getData(num)
print(result)
