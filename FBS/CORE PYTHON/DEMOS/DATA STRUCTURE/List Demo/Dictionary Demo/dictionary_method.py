dict={1:"shivraj",2:"apple",3:7,4:200000}

print(dict)



print(dict.clear()) #to clear the dictionary
dict2=dict.copy()  #to copy the dictionary and assing to other variable
print(dict[4])  #to get value that is present at customize index 4  ,but if key not present will give error
print(dict.get(4,"key not exists"))  #it will return msg you want when key not present
print(dict.items())  #to get key and values in open parenthesis in key value format
print(dict.keys())  #to get only keys
print(dict.pop(2))  #to remove value and key in dict that is present at index
print(dict.popitem())  #to remove last key and value from dictionary
print(dict.update({4:"Talented",5:"GOAT"}))  # to  update the in dictionary
print(dict.values())  #to get only values







input("enter")