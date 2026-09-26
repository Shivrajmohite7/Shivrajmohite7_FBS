# python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/DATA STRUCTURE/String Demo/count_occ_of_char.py"

# count occurence of character in string 

st="vishnu"
char="v"
print(st.count(char))

# ___________________________________________________________________

st=input("enter:")

for i in st:
    c=0
    for j in st:
        if i==j:
            c=c+1
    print(c)

# ___________________________________________________________________


st=input("enter:")
for i in set(st):
    print(i, st.count(i))

