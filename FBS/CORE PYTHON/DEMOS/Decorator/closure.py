# Remember a number
# Create a closure that takes a number and 
# returns an inner function that prints that number.

# def outer(x):
#     def inner():
#         print(x)
#     return inner

# res=outer(10)
# res()


# def outer(x):
#     def inner(y):
#         print(x+y)
#     return inner

# res=outer(10)
# print(res(5))


def deco(a):
    def wrap(*args):
        for i in args:
            if i%2==0:
                print("even")
            else:
                print("odd")
        a(*args)       
    return wrap

@deco
def ev_odd(a):
    pass
ev_odd(3)


# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/closure.py"
