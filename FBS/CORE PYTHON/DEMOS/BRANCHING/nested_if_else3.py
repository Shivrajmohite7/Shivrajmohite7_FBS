
# 3.LOGIN SYSTEM

username=(input("Enter Username:"))
password=int(input("Enter Password:"))

if username=='admin123':
    if password==1234:
        print("Password verified")
    
    else:
        print("Something went wrong")
else:
    print("Invalid username")  

# input("enter")