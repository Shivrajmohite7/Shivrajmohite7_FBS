# Python Program to Remove the Given Key from a Dictionary

dic = {1: "messi", 2: "ronaldo", 11: "amitabh", "neymar": 11}

key = input("Enter keys separated by spaces: ").split()

for i in key:
    if i.isdigit():
        dic.pop(int(i), None)
    else:
        dic.pop(i, None)

print(dic)