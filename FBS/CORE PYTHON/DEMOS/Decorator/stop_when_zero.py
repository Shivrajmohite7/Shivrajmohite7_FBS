
# decorator to stop and say cant perfom when divion is by zero 

def decorator(a):
    def wrapper(*args):
        for i in args:
            if i == 0:
                print("cant perform")
                return
        a(*args)
    return wrapper

@decorator
def getData(x,y):
    z=x/y
    print(z)

x=int(input("enter:"))
y=int(input("enter:"))
result=getData(x,y)