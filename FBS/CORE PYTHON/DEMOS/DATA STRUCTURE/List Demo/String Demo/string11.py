

# strng rotation check

def getdata(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in (s1+s1)


s1=input("enter:")
s2=input("enter:")

result=getdata(s1,s2)
print(result)



# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string11.py"