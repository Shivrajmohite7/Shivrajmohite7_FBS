from myexception import MyException
try:
    age=int(input("enter age:"))
    if age<=0:
        raise MyException(age)
except MyException as m:
    print(m)

# except Exception as e:
#     print(e)
    
# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/EXCEPTION HANDLING/abc.py"