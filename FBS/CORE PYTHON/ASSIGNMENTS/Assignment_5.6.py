
# 6. Write a program to print first n prime numbers.

# n means dont set start just give end range
n=int(input("enter:"))
i=2
for i in range(i,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
