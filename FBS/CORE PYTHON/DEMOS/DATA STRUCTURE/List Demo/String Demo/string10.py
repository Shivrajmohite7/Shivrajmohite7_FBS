# # Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string10.py"


inp1=input("enter the string 1:")
inp2=input("enter then string 2:")

ana=True
for i in inp1:
    if i not in inp2:
        ana=False
for i in inp2:
    if i not in inp1:
        ana=False

if ana:
    print("anagram")
else:
    print("not anagram")
    
    




