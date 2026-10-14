try:
    age=int(input("enter age:"))
    if age<=0:
        raise ZeroDivisionError("age cant be negative")
    else:
        print(age)

except Exception as e:
    print(e)
    
    
