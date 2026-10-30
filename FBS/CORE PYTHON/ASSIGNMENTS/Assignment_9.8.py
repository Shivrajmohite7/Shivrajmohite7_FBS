def prime(n, i=2):
    if n <= 1:
        return False

    if i * i > n:
        return True

    if n % i == 0:
        return False

    return prime(n, i + 1)


n = int(input("Enter number: "))

if prime(n):
    print("Prime Number")
else:
    print("Not Prime Number")