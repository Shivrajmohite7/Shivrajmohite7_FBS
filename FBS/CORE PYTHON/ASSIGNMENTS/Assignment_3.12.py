# 12. Check 3-digit number palindrome

num = int(input("Enter a three-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == c:
    print("Palindrome")
else:
    print("Not a palindrome")