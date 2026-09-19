# Create a sample list
fruits = ["apple", "banana", "cherry", "banana"]

# 1. append(element) - Adds an item to the end
fruits.append("date")
print("1. append:", fruits)

# 2. extend(iterable) - Appends elements from another list/iterable
fruits.extend(["elderberry", "fig"])
print("2. extend:", fruits)

# 3. insert(index, element) - Inserts an item at a specific position
fruits.insert(1, "apricot")
print("3. insert:", fruits)

# 4. remove(element) - Removes the first occurrence of a value
fruits.remove("banana")
print("4. remove:", fruits)

# 5. pop([index]) - Removes and returns element at index (default: last)
popped_item = fruits.pop(2)
print(f"5. pop: removed '{popped_item}', list is now: {fruits}")

# 6. index(element) - Returns index of first occurrence
banana_index = fruits.index("banana")
print("6. index of 'banana':", banana_index)

# 7. count(element) - Returns number of occurrences
count_banana = fruits.count("banana")
print("7. count of 'banana':", count_banana)

# 8. sort(key=None, reverse=False) - Sorts the list in place
fruits.sort()
print("8. sort:", fruits)

# 9. reverse() - Reverses the order of the list in place
fruits.reverse()
print("9. reverse:", fruits)

# 10. copy() - Returns a shallow copy of the list
fruits_copy = fruits.copy()
print("10. copy:", fruits_copy)

# 11. clear() - Removes all elements from the list
fruits.clear()
print("11. clear:", fruits)