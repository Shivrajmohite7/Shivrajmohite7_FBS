
# Write a Python program to remove the intersection of a second set
# with a first set.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

for i in b:
    if i in a:
        a.remove(i)
print(a)