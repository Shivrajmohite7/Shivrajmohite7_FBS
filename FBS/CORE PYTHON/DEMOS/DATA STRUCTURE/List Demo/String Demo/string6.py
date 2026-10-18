# first non repeating character

inp="programming"

for i in inp:
    count=0
    for j in inp:
        if i == j:
            count=count+1
    if count==1:
        print("first non-repating :",i)
        break
    

    
# inp=input("enter:")
# for i in inp:
#     count=0
#     for j in inp:
#         if i == j:
#             count=count+1
#     if count==1:
#         print("first non-repeating character:",i)
#         break
    
# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string6.py"