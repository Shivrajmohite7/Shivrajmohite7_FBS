# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def getData(n):
    a=0
    b=1
    for i in range(n+1):
        yield a
        a,b=b,a+b
        
n=int(input("enter:"))
result=getData(n)


print(next(result))
print(next(result))
print(next(result))

# for i in result:
#     print(i)

# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Assignment_19.8.py"