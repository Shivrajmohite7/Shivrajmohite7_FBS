a = {10, 20, 30, 40, 50}
b = {20, 30, 60, 70}

missing_b = a - b
missing_a = b - a

print("Missing in second set:", missing_b)
print("Missing in first set:", missing_a)