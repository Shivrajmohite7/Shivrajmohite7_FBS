# decorator to print string only if greate the 5 words 

def decorator(a):
    def wrapper(*args):
        for i in args:
            if len(i)>5:
                a(*args)
            else:
                print("cant perform")
                return 
    return wrapper

@decorator

def st(x):
    print(x)

ax=input("enter:")
res=st(ax)
