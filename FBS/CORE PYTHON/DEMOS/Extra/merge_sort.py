def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point to split the array into two halves
        mid = len(arr) // 2
        
        # Divide the array elements into two temporary sub-lists
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize iterators for left half (i), right half (j), and main array (k)
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Driver code to test the implementation
if __name__ == '__main__':
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {data}")
    
    merge_sort(data)
    print(f"Sorted array:   {data}")
