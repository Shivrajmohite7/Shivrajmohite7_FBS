# Write a decorator that checks whether the argument
# passed to a function is a number and if number dont perform.

def decorator(a):
    def wrapper(*args):
        if isinstance(args[0],(int,float)):
            print("it is int and float cant perform")
     
        else:
            a(*args)
    return wrapper

@decorator
def num(a):
    print(a)

num=10
num("done")
#  python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco8.py"