days = int(input("Enter total days: "))

years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)