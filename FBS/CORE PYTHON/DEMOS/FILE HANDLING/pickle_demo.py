import pickle

# Creating Python data
data = [10, 20, 30, 40, 50]
count=0
for i in range(len(data)):
    if i % 2!=0:
        i+4
        print(data[i])
# Open file for writing
f = open("data.dat", "wb")

# Save data
pickle.dump(data, f)

# Close file
f.close()


# Open file for reading
f = open("data.dat", "rb")

# Get data back
data = pickle.load(f)

print(data)

# Close file
f.close()

# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/FILE HANDLING/pickle_demo.py"