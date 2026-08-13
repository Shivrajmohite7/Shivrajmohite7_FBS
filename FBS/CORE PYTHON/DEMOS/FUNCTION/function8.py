#  neglect positional paramaeter concept
# to assign value to parameter in function call
# prameter name in function defination
# flow from right to left


def emp(id,name,sal,dept):
    print("id:",id)
    print("name:",name)
    print("sal:",sal)
    print("dept:",dept)

emp(dept="IT",name="mike",id=7,sal=200000) #--go to according to seq of arguments
print("________________________________")
emp(101,name="mike",dept="it",sal=200000) #---go according to seq of parameter

input("enter")
