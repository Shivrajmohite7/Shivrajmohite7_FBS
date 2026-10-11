class Product:
    def __init__(self,prod_id=None,prod_name=None,prod_price=None,prod_quantity=None):
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.prod_price=prod_price
        self.prod_quantity=prod_quantity
        
    
    def __str__(self):
        return (f"ID:{self.prod_id}\nNAME:{self.prod_name}\nPRICE:{self.prod_price}\nQUANTITY:{self.prod_quantity}\n")
    
    def __del__(self):
        print("destroyed")
    
b1=Product()
print(b1)
b2=Product(123,"Pencil",50,"10")
print(b2)


# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/ASSIGNMENTS/Assignment_15.2.py"