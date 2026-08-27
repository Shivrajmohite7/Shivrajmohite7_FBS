num = int(input("Enter number: "))
summ = 0

for i in str(num):
    summ = summ + int(i) ** 3

if summ == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
