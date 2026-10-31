a = ["apple", "banana", "apple", "orange",
     "banana", "apple"]

unique = set(a)

for i in unique:
    count = 0

    for j in a:
        if i == j:
            count += 1

    print(i, ":", count)