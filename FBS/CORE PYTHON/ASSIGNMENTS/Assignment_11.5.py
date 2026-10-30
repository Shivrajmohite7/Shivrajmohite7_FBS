def sort_length(l):
    l.sort(key=len)
    return l


l = ["apple", "kiwi", "banana", "fig", "mango"]

print(sort_length(l))