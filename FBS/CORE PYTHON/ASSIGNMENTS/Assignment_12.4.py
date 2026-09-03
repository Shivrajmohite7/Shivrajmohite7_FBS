# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

txt=input("enter text:")

txt=txt[-1]+txt[1:-1]+txt[0]
print(txt)