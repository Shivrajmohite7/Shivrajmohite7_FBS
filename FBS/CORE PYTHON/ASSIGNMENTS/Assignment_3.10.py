
# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

male=int(input("Enter Age Of Male:"))
female=int(input("Enter Age Of Female:"))

if male>=21:
    if female>=18:
        print("Elgible To Marry")
    else:
        print("Not Eligble")
else:
    print("Not Eligble")
