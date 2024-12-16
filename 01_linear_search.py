def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

numbers = list(map(int, input("Enter an array (space separated values): ").split()))
key = int(input("Enter the number you want to found: ").strip())

result = linear_search(numbers, key)

if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")
