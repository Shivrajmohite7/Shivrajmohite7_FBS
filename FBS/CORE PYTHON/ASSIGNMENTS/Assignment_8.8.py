#  Write a program to check if entered year is a leap year or not.

def leap(yr):
    for i in range(1):
        if yr%400==0 or (yr%4==0 and yr!=100):
            return(f"year {yr} is leap")
        else:
            return(f"year {yr} is not leap")

year=int(input("enter:"))
res=leap(year)
print(res)
            