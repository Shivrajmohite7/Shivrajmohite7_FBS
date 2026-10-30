def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def series(n):
    if n == 0:
        return 0
    return fact(n) + series(n - 1)


n = int(input("Enter number: "))

print("Sum of Series:", series(n))