# check wether passed argument is list or not 

def decorator(a):
    def wrapper(*args):
        for i in args:
            if isinstance(i,list):
                print("it is list")
            else:
                a(*args)

    return wrapper


@decorator
def check(*args):
    print("dne")

check([10,29],[40,50])
# check("done")


#  python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco9.py"






#  python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/Decorator/deco8.py"
