# we can pass function as paramenter 

def Fact():
    n=int(input("enter:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    
def add(a,b,z):
    print(a+b)
    z()
result=add(10,10,Fact)
