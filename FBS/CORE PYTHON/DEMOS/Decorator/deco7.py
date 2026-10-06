
# Create a decorator that works with a function taking two arguments:


def decorator(a):
    def wrapper(*args):
        print("started")
        a(*args)
    return wrapper

@decorator
def add(x,y):
    print(x+y)

add(10,20)