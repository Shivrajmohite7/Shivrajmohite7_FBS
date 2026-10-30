def snake_pattern():
    n = 1

    for i in range(10):
        row = []

        for j in range(10):
            row.append(n)
            n += 1

        if i % 2 == 1:
            row.reverse()

        print(row)


snake_pattern()