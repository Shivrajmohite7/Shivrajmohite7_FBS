# Python Program to Multiply All the Items in a Dictionary

dic={1:5,2:2,3:3,4:4}
mul1=1
mul2=1
for k,v in dic.items():
    mul1=mul1*v
    mul2=mul2*k
print("keys:",mul2)
print("values:",mul1)
