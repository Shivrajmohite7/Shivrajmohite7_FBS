
# merge 2 dictionary in one 

dic1={1:"amitabh",2:"virat",3:"messi",4:"sharukh"}
dic2={11:"sunil",23:"sachin",44:"neymar"}

new={}

for k,v in dic1.items():
    if k not in new:
        new[k]=v

for kk,vv in dic2.items():
    if kk not in new:
        new[kk]=vv
print(new)
        