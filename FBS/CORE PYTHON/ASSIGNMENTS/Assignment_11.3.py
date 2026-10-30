def sort_list(l):
    l.sort(key=lambda x: x[1])
    return l


l = [[1, 5], [2, 3], [3, 8], [4, 1]]

print(sort_list(l))