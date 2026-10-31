class Television:

    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def Accept(self):

        self.model_no = int(input("Enter Model Number: "))

        if len(str(abs(self.model_no))) > 4:
            raise ValueError("Model number cannot have more than 4 digits")

        self.screen_size = float(input("Enter Screen Size: "))

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        self.price = float(input("Enter Price: "))

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")

    def Display(self):

        print("\n----- Television Details -----")
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs.", self.price)


# Main program

t1 = Television()

try:
    t1.Accept()

except ValueError as e:
    print("Exception:", e)

    print("Replacing all values with default values")

    t1.model_no = 0
    t1.screen_size = 0
    t1.price = 0

t1.Display()