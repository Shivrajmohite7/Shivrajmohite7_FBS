
# create function that rimics range 


def genrateData(start,stop,step):
    while start<stop:
        yield start
        start=start+step
   
start=int(input("enter:"))     
stop=int(input("enter:"))     
step=int(input("enter:"))     

res=genrateData(start,stop,step)
print(next(res))
print(next(res))
print(next(res))