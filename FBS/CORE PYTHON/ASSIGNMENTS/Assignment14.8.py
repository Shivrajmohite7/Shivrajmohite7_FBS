a = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for i in a:
    key = tuple(sorted(i))

    if key not in groups:
        groups[key] = []

    groups[key].append(i)

for i in groups.values():
    print(i)