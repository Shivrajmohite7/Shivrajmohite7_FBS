# 1.break: to stop the flow of code means code below break will not run
for i in range(1,51):
    if (i==21):
        break;
    print(i)
input("enter")

# 2.else: else will run only when code runs properly
for i in range(1,51):
    # if (i==32):
    #     break;
    print(i)
else:
    print("done")

# 3.continue:to stop current iteration;skip the code in the current turn (iteration) and jump straight to the next turn
for i in range(1,40):
    if (i==3):
        continue
    print(i)
input("enter")

# 4. pass:to neglect expected indented block error
for i in range(1,10):
    pass
input("enter")

