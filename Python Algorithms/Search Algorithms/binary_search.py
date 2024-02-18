def binary_search(numbers, target):
    if len(numbers) == 0:
        return "Target not found"

    mid = len(numbers) // 2
    if numbers[mid] == target:
        return "Target found in list"

    left = numbers[:mid]
    right = numbers[mid+1:]

    if numbers[mid] > target:
        return binary_search(left, target)
    else:
        return binary_search(right, target)


# numbers = [1,2,4,5,7,9,16,96]
# print(binary_search(numbers, 1))
# output: Target found in list