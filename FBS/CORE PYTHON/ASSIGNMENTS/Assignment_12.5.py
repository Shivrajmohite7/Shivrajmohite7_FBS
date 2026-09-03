# 5. Python Program to Count the Number of Vowels in a String

vow="aeiouAEIOU"
txt=input("enter text:")
count=0
for i in txt:
    if i in vow:
        count=count+1
print(count)
