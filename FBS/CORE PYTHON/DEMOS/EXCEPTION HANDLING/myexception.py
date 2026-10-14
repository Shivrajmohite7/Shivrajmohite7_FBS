class MyException(Exception):
    def __init__(self, *args):
        self.age=args
        print("I am in exception class")
    def __str__(self):
        return f"Enter proper age"
        