# to print:

#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I

for i in range(5):
    for j in range(1,6-i):
        print(" ", end=" ")
        
    for j in range(1, 2 * i + 2):
        print(chr(64 + j), end=" ")

    print()
input("enter")
