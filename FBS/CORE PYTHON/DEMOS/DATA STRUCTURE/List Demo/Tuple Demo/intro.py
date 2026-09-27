#1.() denoted by

tu=(10,20,30,40)

#2
tu=(10,) # type will be tuple

#3. immutable

tu[0]=7

# Duplicate Allowed

tu=(10,20,30,30)

#4. Faster than list

# beacuse tuple have 44 bytes and list have 54 bytes 


# 5.to check how much bytes contain
import sys 
print(sys.getsizeof(tu))  

input("enter")