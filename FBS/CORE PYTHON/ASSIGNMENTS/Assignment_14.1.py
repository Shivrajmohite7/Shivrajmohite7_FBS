# elemtns that are in 'a' but not in 'b'
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c=set()
for i in a:
    if i not in b:
        c.add(i)
print(c)
