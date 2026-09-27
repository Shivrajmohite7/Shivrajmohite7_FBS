# common of 2 sets is intersection 
# disjoint means all elemebt sould be diff in both set?
# random element remove randomly pop
# will add mulitp elements by update
# add will add single lelements

s1={10,20,30,40}
s2={30,40,50,60}
s3={50,60}
s4={50,60}

s1.add(70)  # will add element but single not multiple
s1.clear() # will wipeout set elements
s5=s1.copy()  #s5 will get all elements from s1
print(s1.difference(s2))
print(s1.difference_update(s2))
s1.discard(50)  #will remove 50 and if 50 not exists no error will come
print(s1.intersection(s2))  # common of 2 sets is intersection 
s1.intersection_update(s2)  # now s1 value will be onnly 30 nd 40
print(s1.isdisjoint(s3))  # disjoint means all elemnt  sould be diff in both set?
print(s3.issubset(s2))
print(s2.issuperset(s3))
s1.pop()  #will remove any one random element
s1.remove(40)  #element will be remove but if element not there then error will throw 
s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1.union(s2))   #all elements one time within 2 sets
s1.update({7,80,90}) # will add multiple elements
print(s1)

input("enter")