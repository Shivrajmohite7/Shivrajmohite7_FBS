def union(l1, l2):
    result = list(set(l1) | set(l2))
    return result


l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

print("Union:", union(l1, l2))