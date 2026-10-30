def print_hollow_diamond(n):
    # Upper half of the diamond (including the middle row)
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print the characters for the current row
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print the characters for the current row
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage:
n = 5
print_hollow_diamond(n)
