a = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(a[0])):
    s = set()

    for j in a:
        s.add(j[i] if i < len(j) else "")

    if len(s) == 1:
        prefix += a[0][i]
    else:
        break

print("Common prefix:", prefix)