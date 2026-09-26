# string is palindrome or not 

st="bob"
x=st[::-1]
if x==st:
    print("pallindrome")
else:
    print("not")

# _________________________________________________________________________



st="bob"
rev=""

for i in range(len(st)-1,-1,-1):
    rev+=st[i]
if rev == st:
    print("pallindrome")
else:
    print("not")


# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/DATA STRUCTURE/String Demo/String_palindrome.py"