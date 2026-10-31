class Shirt:

    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

        if self.size.lower() == "small":
            self.price = price

        elif self.size.lower() == "medium":
            self.price = price + (price * 10 / 100)

        elif self.size.lower() == "large":
            self.price = price + (price * 20 / 100)

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", self.price)

    def __del__(self):
        print("Shirt object destroyed")


s1 = Shirt()
s2 = Shirt(101, "Formal Shirt", "Formal", 1000, "Small")
s3 = Shirt(102, "Casual Shirt", "Casual", 1000, "Medium")
s4 = Shirt(103, "Party Shirt", "Party Wear", 1000, "Large")

s2.ShowBook()
s3.ShowBook()
s4.ShowBook()