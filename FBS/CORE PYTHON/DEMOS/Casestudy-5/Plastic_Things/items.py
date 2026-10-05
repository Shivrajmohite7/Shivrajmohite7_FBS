class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def view(self):
        print(f"ITEM:{self.name}")
        print(f"PRICE:{self.price}")
        
        

        