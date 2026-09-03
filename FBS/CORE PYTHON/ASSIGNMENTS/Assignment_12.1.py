# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

text="Today is thursday"
new_txt=""

for i in text:
    if i =="a":
        new_txt+="$"
    else:
        new_txt+=i
print(new_txt)