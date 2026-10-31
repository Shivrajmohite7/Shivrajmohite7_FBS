class Distance:

    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):

        total = (self.km * 100000 + self.m * 100 + self.cm +
                 other.km * 100000 + other.m * 100 + other.cm)

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    def __sub__(self, other):

        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 - total2

        if total < 0:
            print("Distance cannot be negative")
            return Distance()

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    def Display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")

    def __del__(self):
        print("Distance object destroyed")


d1 = Distance(2, 500, 50)
d2 = Distance(1, 300, 25)

print("First Distance:")
d1.Display()

print("Second Distance:")
d2.Display()

d3 = d1 + d2
print("Addition:")
d3.Display()

d4 = d1 - d2
print("Subtraction:")
d4.Display()