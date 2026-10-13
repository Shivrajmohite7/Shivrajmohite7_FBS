from book import Book

books={}

while True:
    print("1.Add book:")
    print("2.delte book:")
    print("3.display book:")
    print("4.search book:")
    print("5.exit book:")
    
    ch=int(input("enter above choice:"))

    if ch==1:
        bid = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        price = float(input("Enter price: "))
        author = input("Enter author: ")
        
        b=Book(bid,name,price,author)
        books[bid]=b
        
    elif ch==2:
        bid=int(input("enter bid to delete:"))
        if bid  in books:
            del books[bid]
            print("deleted")

    elif ch==3:
        for bid in books:
            b=books[bid]
            print(b.bid, b.name, b.price, b.author)
            
    elif ch==4:
        bid=int(input("enter bid:"))
        if bid in books:
            b=books[bid]
            print(b.bid, b.name, b.price, b.author)
           
        else:
            print("cant found")             

    elif ch==5:
        break
    else:
        print("invalid")

        

input("enter")