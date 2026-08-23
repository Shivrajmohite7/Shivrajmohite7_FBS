# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

basic = float(input("Enter basic salary: "))

da = 10 / 100 * basic
ta = 12 / 100 * basic
hra = 15 / 100 * basic

total = basic + da + ta + hra

print("Total Salary =", total)
