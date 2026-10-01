def star(n):
    for i in range(1,13):
        for j in range(1,23):
            if i==1 or i==12 or 2*i+j==25:
                print("*",end="")
            else:
                print(" ",end="")
        print()
                
n='*'
star(n)
