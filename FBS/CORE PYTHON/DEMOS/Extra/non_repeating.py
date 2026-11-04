# first non repeating character 

st="aabbcdde"
count=0
for i in st:
    count=0
    for j in st:
        if i == j:
            count=count+1
    if count == 1:
        print(i)
        break
