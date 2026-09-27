
def twoSum(arr, target):

    seen = {}
    # Dictionary to remember:
    # number -> index
    for i in range(len(arr)):
        # Go through each number
        needed = target - arr[i]
        # Find what number we need
        # Example: target = 9, current = 2
        # needed = 9 - 2 = 7
        if needed in seen:
            # Check: Have we already seen the needed number?
            return [seen[needed], i]
            # Yes!
            # seen[needed] = index of the previous number
            # i = index of current number
        seen[arr[i]] = i
        # We haven't found the pair yet,
        # so remember current number and its index

arr = [7,8 , 11, 4]
target = 15
result = twoSum(arr, target)
print(result)

