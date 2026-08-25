# def selectionsort(li):
#     size=len(li)
#     for i in range(0,size-1):
#         min_ind=1
#         for j in range(i+1,size):
#             if (li[j]<li[min_ind]):
#                 min_ind=j
#         li[i],li[min_ind]=li[min_ind],li[i]
#     print(li)


# li=[10,40,50,23,563,45]
# print(f"before",li)

# selectionsort(li)
# print(f"after",li)




def selectionsort(li):
    size = len(li)

    for i in range(0, size - 1):
        min_ind = i

        for j in range(i + 1, size):
            if li[j] < li[min_ind]:
                min_ind = j

        li[i], li[min_ind] = li[min_ind], li[i]


li = [10, 40, 50, 23, 563, 45]

print("Before:", li)

selectionsort(li)

print("After:", li)

input("Enter to exit...")

input("enter")