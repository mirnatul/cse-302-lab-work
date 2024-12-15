def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    :param left: Sorted left half.
    :param right: Sorted right half.
    :return: Merged sorted list.
    """
    sorted_list = []
    i = j = 0

    # Compare elements from both halves and add the smallest to the sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements from the left half (if any)
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Add remaining elements from the right half (if any)
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print("Sorted list:", sorted_numbers)
