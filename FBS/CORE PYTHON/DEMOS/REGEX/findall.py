import re

data="virat age is 36 or 37"

d=re.findall(r"\d{2}",data)  #-2 for two digits ,if no 2 single digits
print(d)

d=re.search(r"\d+",data)  
print(d.group())



# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/REGEX/findall.py"