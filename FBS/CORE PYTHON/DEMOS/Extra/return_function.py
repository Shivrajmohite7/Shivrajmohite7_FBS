
# return one fucntion from another
def add():
    a=int(input("enter:"))
    b=int(input("enter:"))
    c=a+b
    print(c)

def mul():
    x=int(input("enter:"))
    y=int(input("enter:"))
    z=x*y
    print(z)
    return add

res=mul()
res()