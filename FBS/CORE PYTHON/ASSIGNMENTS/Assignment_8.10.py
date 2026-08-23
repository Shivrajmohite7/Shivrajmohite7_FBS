#  Write a program to check if entered number is a palindrome or
# not.

def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return "The number is a palindrome"
    else:
        return "The number is not a palindrome"


num = int(input("Enter a number: "))
print(palindrome(num))
