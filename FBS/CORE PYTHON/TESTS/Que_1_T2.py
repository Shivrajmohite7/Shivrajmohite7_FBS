year =int(input("enter year:"))
for i in range(1):
    if year % 400 == 0 or (year % 4 == 0 and year %100 != 0):
        print(f"{year} is Leap Year")
    else:
        print("Not a leap year")


input("enter")