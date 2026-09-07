
# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

txt1=input("enter text1:")
txt2=input("enter text2:")

count1=0
count2=0
for i in txt1:
    count1=count1+1
for i in txt2:
    count2=count2+1

if count1>count2:
    print("string one is bigger")
elif count2>count1:
    print("string two is bigger")
elif count1==count2:
    print("both are equal")
else:
    print("check again")