def second_largest(l):
    n = len(l)

    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l[-2]


l = [10, 5, 20, 8, 15]

print("Second Largest:", second_largest(l))