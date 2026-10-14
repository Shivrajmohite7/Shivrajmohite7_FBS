try:
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))
    x=num1//num2
    print(x)
    
except ZeroDivisionError as z:
    print(f"Cant be with zero {z}")
    
except ValueError as v:
    print(f"Value Error {v}")

else:
    if x>10:
        print("greater than 10")

    else:
        print("you decide")

finally:
    print("try except finally else")


    
# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/TEEF.py"
