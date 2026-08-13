# topic: keyword-variable-length parameter
# mention 2 asterisk symbols before parameter name in function defination
# passed data stored in dictionary format
# use for loop on dict.items() to get values and keys

# def emp(**data):
#     for key,val in data.items():
#         print(key,":",val)

# emp(id=101,age=23,add="pune",sal=200000,dept="IT")


def emp(**data):

    print(data)

abc=emp(a=10,b=20,c=30,d=40)
print(abc)
