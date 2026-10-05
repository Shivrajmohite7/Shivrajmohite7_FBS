class Order:
    def __init__(self):
        self.items=[]
    def add_item(self,item,qunatity):
        self.items.append((item,qunatity))
        
    def show_order(self):
        for item,quantity in self.items:
            pass
            # print(item.name,"x",quantity)
        
    
    
    
    
    
    
# class Order:
#     def __init__(self):
#         self.items=[]
#     def add_item(self,item,quantity):
#         self.items.append((item,quantity))
    
#     def show_order(self):
#         for item,quantity in self.items:
#             print(item.name,"x",quantity)