text = input("Enter a string: ")

words = 0
characters = 0
in_word = False

for ch in text:
    characters += 1

    if ch != " " and not in_word:
        words += 1
        in_word = True

    elif ch == " ":
        in_word = False

print("Number of words:", words)
print("Number of characters:", characters)
