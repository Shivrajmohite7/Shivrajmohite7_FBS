# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

txt=input("enter:")
res=""

for i in range(len(txt)):
    if i%2==0:
        res=res+txt[i]
print(res)

