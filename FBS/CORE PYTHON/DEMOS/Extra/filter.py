
# filter out negative numbers 

li=[23,4,5,6,7,-10,-11,-12,49,-34,56]
neg=list(filter(lambda a:a<=-1,li))
print(neg)

# filter words that stat with v

li=["Apple","Vishnu","Avocado","Vice City"]
stv=list(filter(lambda a:a.startswith('V'),li))
print(stv)

# filter number divsible by 2 and 3 

li=[6,8,12,15,18,20]
divi=list(filter(lambda x:x%2==0 and x%3==0,li))
print(divi)

# filter words that are in inp1 and inp2

inp1=["vishnu","cat","horse"]
inp2=["vishnu","cat","tortise","parrot"]

wrds=list(filter(lambda x:x in inp2,inp1))
print(wrds)



