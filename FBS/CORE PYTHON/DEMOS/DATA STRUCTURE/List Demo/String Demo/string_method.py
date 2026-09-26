str="FirstBit Solutions"
print(str.capitalize())   #makes only first character captial
print(str.count('BYt'))    #count how much time specific character occured if,if single is wrriten it will count if you wrote word and one char is also not present in list will return 0
print(str.endswith('ps')) #return true or false if it is ended with your given character.
print(str.find('bit'))   #return -1 even one chr is also not present 
print(str.index('bit'))  #will return index and if one also char not present will return 'value error'
print(str.isalnum())  #will return true only if it contains numbers or alphabets ,even spaces is there it will return false
print(str.isalpha()) #only alpahabets no spaces no numbers
print(str.isdigit()) #only digits nothing else no spaces also
print(str.islower()) #all should be is lower
print(str.isupper()) #all should be is uppercase
print(str.replace('Bit','Byte')) #will repalce and if one char also not present it will nor replace nor error
print(str.split(' ')) 
print(str.startswith('Fir')) 
print(str.strip('')) #remove trailing space
print(str.lstrip(''))#remove left trailing space
print(str.rstrip('')) #remove right trailing space
print(str.swapcase())  #capital will be lower ,Lower will be capital
print(str.upper()) #converts to uppercase 
input("enter") 