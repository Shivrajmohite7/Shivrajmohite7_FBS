# Write a decorator that removes duplicate values from a 
# list before passing the list to the function.

def decorator(a):
    def wrapper(args):
        print("started")
        lii=[]
        for i in args:
            if i not in lii:
                lii.append(i)
        print(lii)
        print("stopped")
    return wrapper
@decorator

def aa(li):
    pass

li=[11,22,3,4,4,5,5,6]
aa(li)

@decorator
def b(c):
    pass
c=[1,1,1,2,2,3,4,5]
b(c)

# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco10.py"
# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco10.py"
