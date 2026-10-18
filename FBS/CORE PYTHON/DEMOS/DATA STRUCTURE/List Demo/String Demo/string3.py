# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string3.py"

# count vowels and consonants

inp=input("enter string:")
conso="bcdfghjklmnpqrstvwxyz"

count1=0
count2=0

for i in inp.lower():
    if i in "aeiouAEIOU":
        count1=count1+1
    elif i in conso:
        count2=count2+1
       
print("vowels:",count1) 
print("cosonants:",count2)

