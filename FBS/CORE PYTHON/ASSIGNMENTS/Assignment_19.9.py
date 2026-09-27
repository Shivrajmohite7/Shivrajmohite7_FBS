# pallindrome lazily and infinitely.

def getData():
    i=1
    while True:
        x=int(str(i)[::-1])
        if x==i:
            yield i
        i+=1
result=getData()  
print(next(result))
print(next(result))
print(next(result))
print(next(result))








# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Assignment_19.9.py"