
# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passenger=int(input("enter passengers:"))
total=0
for  i in range(1,passenger+1):
    print(f"passangers={i}")

    ticket=int(input("Enter ticket cost:"))
    age=int(input("Enter age:"))

    if age<12:
       ticket=ticket-(ticket*30/100)
       print(f"Child Ticket ={ticket}")
    elif age>59:
        ticket=ticket-(ticket*50/100)
        print(f"Senior Citizen Ticket ={ticket}")
    else:
        print(f"Pay Full {ticket}")
    total=total+ticket
print(total)
