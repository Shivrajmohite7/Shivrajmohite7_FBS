
# 13. Python Program to count number of digits and letters in a string.

txt=input("enter text:")
dig=0
letter=0

for i in txt:
    if i>='0' and i<='9':
        dig=dig+1
    elif (i>='A' and i<='Z') or (i>='a' and i<='z'):
        letter=letter+1

print(dig)
print(letter)