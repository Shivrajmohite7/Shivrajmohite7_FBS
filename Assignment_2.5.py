# WAP to calculate selling price of book based on cost price and discount.

cost = float(input("ENTER BOOK PRICE: "))
discount = float(input("ENTER DISCOUNT GIVEN: "))

discount_amount = cost * discount / 100
sp = cost - discount_amount

print("DISCOUNT AMOUNT:", discount_amount)
print("SELLING PRICE:", sp)
