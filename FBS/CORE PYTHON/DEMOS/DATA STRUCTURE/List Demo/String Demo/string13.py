# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string13.py"

wrds="abcdefghijklmnopqrstuvwxyz"
new=""
inp=input("enter:")
for i in inp.lower():
    if i in wrds:
        new+=i
print(new)