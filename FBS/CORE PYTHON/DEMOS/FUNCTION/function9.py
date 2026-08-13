#   topic: variable length parameter
# to pass multiple values to function

# passed values are stored in tuple format
# use for loop to iterate/performing actions from tuple

def add(*data):
    sum=0
    for val in data:
        sum+=val
    return sum

res=add(10,20,30,40,50)
print(res)


