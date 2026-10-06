# Square
# Create a decorator for a function square(n) that prints 
# "Calculating square" before calling it.


def decorator(a):
    def wrapper(*args):
        print("Calculating Square")
        a(*args)
    return wrapper

@decorator
def square(n):
    print(n**2)
nn=int(input("enter:"))
square(nn)







# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco2.py"