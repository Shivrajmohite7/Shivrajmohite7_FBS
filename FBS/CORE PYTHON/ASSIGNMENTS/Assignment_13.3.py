# Python Program to Check if a Given Key Exists in a Dictionary or Not

dic={1:"messi",2:"ronaldo",3:"shahrukh",4:"dhoni"}
key=input("enter key:")
if key in dic or (key.isdigit() and int(key) in dic):
    print("key exists")
else:
    print("key not exists")
