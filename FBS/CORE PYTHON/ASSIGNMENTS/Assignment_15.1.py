class Book:
    def __init__(self,book_id=None,book_name=None,book_price=None,book_author=None):
        self.book_id=book_id
        self.book_name=book_name
        self.book_price=book_price
        self.book_author=book_author
        
    
    def __str__(self):
        return (f"{self.book_id}\n{self.book_name}\n{self.book_price}\n{self.book_author}\n")
    
    def __del__(self):
        print("destroyed")
    
b1=Book()
print(b1)
b2=Book(123,"Python:Programming",500,"abc")
print(b2)


# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Assignment15.1.py"