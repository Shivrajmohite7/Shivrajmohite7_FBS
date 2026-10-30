def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)


n = int(input("Enter number: "))

print("Sum:", total(n))