# remove duplicates from string  

inp="programming"
new=set()
neww=""
for i in inp:
    if i not in new:
        new.add(i)
        if i in new:
            neww+=i
print(neww)



# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string9.py"