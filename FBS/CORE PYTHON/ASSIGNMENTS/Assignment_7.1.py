n = 5

for i in range(2 * n):
    for j in range(2 * n - 1):
        if j == abs(n - 1 - i) or j == 2 * n - 2 - abs(n - 1 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()