class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

    def Display(self):
        print(self.real, "+", self.imag, "i")

    def __del__(self):
        print("Object destroyed")


c1 = Complex(10, 5)
c2 = Complex(5, 3)

print("First Complex Number:")
c1.Display()

print("Second Complex Number:")
c2.Display()

c3 = c1 + c2
print("Addition:")
c3.Display()

c4 = c1 - c2
print("Subtraction:")
c4.Display()