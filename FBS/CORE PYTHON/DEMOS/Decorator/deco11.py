# Write a decorator that prevents a function 
# from executing if the input string is empty.

# def decorator(a):
#     def wrapper(inp):
#         if inp=="":
#             print("empty string")
#         else:
#             a(inp)
#     return wrapper

# @decorator
# def st(a):
#     print("function exceuted")
# inp=input("enter:")
# st(inp)

# @decorator
# def st1(a1):
#     print("function exceuted")
# inp1=input("enter:")
# inp2=input("enter:")
# inp3=input("enter:")
# st1(inp1)
# st1(inp2)
# st1(inp3)


def deocrator(a):
    def wrapper(*args):
        for i in args:
            if i == "":
                print("empty")
                return
       
        a(*args)
    return wrapper


@deocrator

def xyz(inp1,inp2):
    print("printed inp1")
    print("printed inp2")
    
inp1=input("enter:")
inp2=input("enter:")
xyz(inp1,inp2)



# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco11.py"