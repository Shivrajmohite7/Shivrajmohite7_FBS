# 2.check string is pallindrome or not 

inp=input("enter string:")
rev=""

for i in inp:
    rev=i+rev
if rev==inp:
    print("pallindrome")
else:
    print("not pallindrome")
    
    
# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string2.py"
