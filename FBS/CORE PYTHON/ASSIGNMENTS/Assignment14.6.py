a = [2, 5, 3, 8, 10, -20]

maximum = a[0] * a[1]
num1 = a[0]
num2 = a[1]

for i in range(len(a)):
    for j in range(i + 1, len(a)):

        product = a[i] * a[j]

        if product > maximum:
            maximum = product
            num1 = a[i]
            num2 = a[j]

print("Numbers:", num1, num2)
print("Maximum product:", maximum)