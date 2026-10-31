a = [10, 20, 10, 30, 10, 40]

n = int(input("Enter number to remove: "))

b = []

for i in a:
    if i != n:
        b.append(i)

print(b)