# python program to remove given key from dictionary 

dic={1:12,2:"amitabh","messi":10,"ronaldo":7}
rm=input("enter key:")
if rm.isdigit():
    rm=int(rm)
if rm in dic:
    del dic[rm]

print(dic)
