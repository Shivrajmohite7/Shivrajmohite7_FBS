
# 10. WAP to check if given number is Perfect Number.

sum = 0
num = int(input("Enter number: "))

for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(f"{num} is perfect number")
else:
    print("Not a perfect number")