a = [10, 20, 10, 30, 10, 40]

n = int(input("Enter number: "))

count = 0

for i in a:
    if i == n:
        count += 1

if count > 0:
    print("Element is present")
    print("Occurrences:", count)
else:
    print("Element is not present")