# 3. Python Program to Detect if Two Strings are Anagrams


txt1=input("enter string1:")
txt2=input("enter string2:")

if len(txt1)!=len(txt2):
    print("not anagram")
else:
    for i in txt1:
        if txt1.count(i) != txt2.count(i):
            print("not anagram")
            break
        else:
            print("anagram")
            break
