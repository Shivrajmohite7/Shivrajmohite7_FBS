area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter interior painting cost per sq.ft: "))
exterior_cost = float(input("Enter exterior painting cost per sq.ft: "))

total_area = area * 2

interior_total = total_area * interior_cost
exterior_total = total_area * exterior_cost

total_cost = interior_total + exterior_total

print("Total wall area =", total_area)
print("Interior painting cost =", interior_total)
print("Exterior painting cost =", exterior_total)
print("Total painting cost =", total_cost)
