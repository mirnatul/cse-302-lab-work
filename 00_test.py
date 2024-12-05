def bs(arr, key):
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

numbers = list(map(int, input().split()))
key = int(input().strip())

result = bs(numbers, key)
print(result)