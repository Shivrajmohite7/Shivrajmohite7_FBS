# print repeated words 

# inp="programming"

# for i in set(inp):
#     count=0
#     for j in inp:
#         if i == j:
#             count=count+1
#     if count>1:
#         print(i)

inp=input("enter:")
for i in set(inp):
    count=0
    for j in inp:
        if i == j:
            if i != " ":
                count=count+1
    if count>1:
        print(i)











# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/Extra/string7.py"