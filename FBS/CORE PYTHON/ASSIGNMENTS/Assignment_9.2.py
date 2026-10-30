def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def armstrong(n, power):
    if n == 0:
        return 0

    digit = n % 10
    return digit ** power + armstrong(n // 10, power)


n = int(input("Enter number: "))

power = count_digits(n)

if armstrong(n, power) == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")