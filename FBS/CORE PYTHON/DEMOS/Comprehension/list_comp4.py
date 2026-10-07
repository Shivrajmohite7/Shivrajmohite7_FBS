
# combine list and print word grater than 4 words

li = [["apple", "banana"], ["cat", "dog"], ["orange"]]

easy=[j for i in li for j in i if len(j)>4]
print(easy)