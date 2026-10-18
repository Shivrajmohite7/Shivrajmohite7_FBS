# count frequency of each character in string 

inp=input("enter:")
new={}

for i in inp:
    if i != " ":
        if i not in new:
            new[i]=1
        else:
            new[i]+=1
print(new)
            