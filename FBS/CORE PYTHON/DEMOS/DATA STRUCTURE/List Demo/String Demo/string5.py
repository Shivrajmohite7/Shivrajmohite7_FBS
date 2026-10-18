# count freq of single word that user enters in string format

inp1=input("enter string:")
inp2=input("enter character:")

count=0
for i in inp1:
    if i==inp2:
        count=count+1
print("character:",inp2,"count is",count)
