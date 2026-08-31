# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

total=0

for i in range(5):
    price=float(input("enter price:"))
    total=total+price

gst=total*18/100
total_gst=total+gst
print(f"Total after Adding GST:{total_gst}")


input("enter")
