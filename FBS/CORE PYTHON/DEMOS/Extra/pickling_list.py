import pickle
li=list(map(int,input("enter numbers:").split()))

with open("C:/Users/TUTION/Desktop/practice/stud.dat",'wb')as f:
    pickle.dump(li,f)
    
with open("C:/Users/TUTION/Desktop/practice/stud.dat",'rb') as f:
    data=pickle.load(f)

# x=data.append(34)
max=data[0]
for i in range(len(data)):
    if data[i]>max:
        max=data[i]
print(max)
    

with open("C:/Users/TUTION/Desktop/practice/stud.dat",'wb')as f:
    pickle.dump(data,f)
    print(max)
    
    