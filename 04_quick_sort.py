def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [] 
    middle = []
    right = []

    for element in arr:
        if element < pivot:
            left.append(element) 
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)
    
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return sorted_left + middle + sorted_right

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
