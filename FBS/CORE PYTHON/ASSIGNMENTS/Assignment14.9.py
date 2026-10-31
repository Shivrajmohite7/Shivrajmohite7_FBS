a = [1, 2, 3, 4, 5, 6, 7]

target = int(input("Enter target: "))

result = set()

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):

            if a[i] + a[j] + a[k] == target:
                result.add((a[i], a[j], a[k]))

print("Combinations:", result)