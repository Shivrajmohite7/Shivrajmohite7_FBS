class Shirt:
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print(f"{self.sid}\n{self.sname}\n{self.type}\n{self.price}\n{self.size}")

    def __del__(self):
        print("Destroyed")


s1 = Shirt()
print("Shirt 1:")
s1.ShowBook()

print("------------------")

s2 = Shirt(101, "Formal Shirt", "Formal", 800, "Large")
print("Shirt 2:")
s2.ShowBook()