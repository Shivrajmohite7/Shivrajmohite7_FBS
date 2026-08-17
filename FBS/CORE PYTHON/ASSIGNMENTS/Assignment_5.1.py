
# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
    
username = "admin1234"
password = 1234

for i in range(1,4):
    user=input("enter user:")
    passw=int(input("enter password:"))

    if user==username and password==passw:
        print("corect")
        break
    else:
        print("incorect")

