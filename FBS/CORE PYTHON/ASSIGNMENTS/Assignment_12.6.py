# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen


txt=input("enter:")
res=""

for i in txt:
    if i == " ":
        res+="-"
    else:
        res+=i
print(res)