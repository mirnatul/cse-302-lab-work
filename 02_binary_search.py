def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

numbers = list(map(int, input("Enter an sorted array (space separated values): ").split()))
key = int(input("Enter the number you want to found: ").strip())

result = binary_search(numbers, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
