
txt1=input("enter:")
res=""
for i in txt1:
    if i == " ":
        res+="-"
    else:
        res+=i
print(res)