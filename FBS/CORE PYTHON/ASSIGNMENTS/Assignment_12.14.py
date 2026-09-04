
# 14. Python Program to count the occurrences of each word in a string.
txt=input("enter:")
done=[]

for i in txt:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        if i not in done:
            print(i,":",txt.count(i))
            done.append(i)

