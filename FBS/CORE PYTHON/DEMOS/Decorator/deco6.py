# Write a decorator for a division function that prevents division by zero.


# def decorator(a):
#     def wrapper(*args):
#         if args[1]==0:
#             print("cant perform")
#         else:
#             a(*args)
#     return wrapper


# @decorator

# def division(a,b):
#     print(a/b)
# division(10,0)
# division(5,102)


def decorator(a):
    def wrapper(*args):
        if args[1]==0:
            print("cant perform")
        else:
            a(*args)
    return wrapper
            
@decorator
def division(a,b):
    print(a/b)

division(10,2)
division(10,0)



# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco6.py"
