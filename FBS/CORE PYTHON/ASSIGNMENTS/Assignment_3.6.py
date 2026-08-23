
# Write a program to calculate profit or loss.

cp=float(int(input("enter cost_price:")))
sp=float(int(input("enter sp_price:")))

sum=cp-sp
summ=sp-cp

if cp>sp:
    print(f"It Is Loss Of:{sum}")
elif sp>cp:
    print(f"It Is Profit Of:{summ}")
else:
    print("No Profit No Loss")
