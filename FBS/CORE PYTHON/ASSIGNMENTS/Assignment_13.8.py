# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

inp=input("enter inp:")
dic={}

for i in inp.split():
    if i in dic and i != " ":
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)
        