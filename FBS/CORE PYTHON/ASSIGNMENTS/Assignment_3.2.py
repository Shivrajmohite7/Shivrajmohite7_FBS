# Write a program to input any alphabet and check whether it is vowel or consonant.

abc=input("enter alphabet:")
vow=["a","e","i","o","u","A","E","I","O","U"]

if len(abc)!=1 or not abc.isalpha():
    print("ENTER ONLY ONE LETTER AND NO DIGITS")
elif abc in vow:
    print("IT IS VOWEL")
else:
    print("IT IS CONSONANT")

