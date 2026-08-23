

# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
user_id=input("enter user_id:")
password=int(input("enter password:"))

if user_id=="admin_1234" and password==1234:
    a=random.randint(1000,2000)
    print(a)
    num=int(input("enter number genrated: "))
    if num==a:
        print("verified")
    else:
        print("try again")
else:
    print("invalid credentials")
