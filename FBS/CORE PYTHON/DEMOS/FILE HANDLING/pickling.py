import pickle
f=open("emp.dat","wb")
print(f.tell())

pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
fr=open("emp.dat",'rb')
f.seek(0)

data=pickle.load(fr)
data1=pickle.load(fr)
data2=pickle.load(fr)
data2=pickle.load(fr)

print(data)
print(data1)
print(data2)