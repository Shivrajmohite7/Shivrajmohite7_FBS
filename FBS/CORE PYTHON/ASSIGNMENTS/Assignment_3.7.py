
# Write a program to check if user has entered correct userid and password.

user_id="admin_1234"
password=1234

User_id=input("Enter UserName:")
Password=int(input("Enter Password:"))

if user_id==User_id and password==Password:
    print("Verfied")
else:
    print("Invalid Credentials")
