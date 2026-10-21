# Python Program to Sum All the Items in a Dictionary
dic={1:10,2:304,4:405,3:10,5:402}
sum1=0
sum2=0
for k,v in dic.items():
    sum1=sum1+v
    sum2=sum2+k
    
print("sum of values:",sum1)
print("sum of keys:",sum2)