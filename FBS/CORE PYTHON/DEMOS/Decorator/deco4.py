# Login Message
# Create a decorator that prints
# "User logged in" before calling a welcome() function.


def decorator(a):
    def wrapper(*args):
        print("logged in")
        a(*args)
    return wrapper


@decorator
def welcome():
    print("welcome")
welcome()








# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco4.py"