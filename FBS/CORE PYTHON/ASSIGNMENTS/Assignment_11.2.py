def merge(l1, l2):
    l3 = l1 + l2
    l3.sort()
    return l3


l1 = [5, 2, 8, 1]
l2 = [7, 3, 6, 4]

print("Merged List:", merge(l1, l2))