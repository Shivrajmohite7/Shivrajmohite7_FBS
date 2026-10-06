
# def multiply(a,b):
#     def multi():
#         return a**b
#     return multi


# dou=multiply(2,2)
# print(dou())



def decorator(a):
    def wrapper(*args):
        print("started")
        a(*args)
    return wrapper

@decorator
def fact(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    print(fact)

result=fact(5)







# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco5.py"