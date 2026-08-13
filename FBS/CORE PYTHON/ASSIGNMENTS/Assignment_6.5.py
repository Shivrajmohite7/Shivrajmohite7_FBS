# to print:

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range(5):
    for j in range(9):
        if i==4 or j==4 or j==1 and i==3 or j==2 and i==2 or j==2 and i==3 or j==3 and i==1 or j==3 and i==2 or j==3 and i==3 or j==5 and i==1 or  j==5 and i==2 or  j==5 and i==3 or j==6 and i==2 or j==6 and i==3 or j==7 and i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
input("enter")