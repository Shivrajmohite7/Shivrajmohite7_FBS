
# 2.VOTING ELGIBILITY BY AGE AND CITIZEN CHECK ALSO.

Age=int(input("Enter The Age:"))
Citizen=input(f"Enter in 'yes/no':")

if Age>17:
    if Citizen=='yes':
        print("CAN VOTE NOW")

    else:{
        print("CANNOT VOTE")
    }
else:{
    print("AGE WRONG")
}

# input("enter")