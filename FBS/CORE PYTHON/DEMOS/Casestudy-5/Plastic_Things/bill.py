class Bill:
    def __init__(self,order):
        self.order=order
        
    def calculate_total(self):
        total=0
        
        
        for item,quantity in self.order.items:
            total=total+(item.price*quantity)
        return total
    
    def show_bill(self):
        for item,quantity in self.order.items:
            amount=item.price*quantity
            
            print(item.name,":","Rs",item.price,"x",quantity,"=",amount)
            
        print("TOTAL:",self.calculate_total())
        
        # item.price