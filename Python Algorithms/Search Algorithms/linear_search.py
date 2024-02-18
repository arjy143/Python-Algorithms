def linear_search(numbers, target):
    for i in range(len(numbers)-1):
        if numbers[i] == target:
            return "Target found"
    return "Target not found"


# numbers = [1,2,4,5,7,9,16,96]
# print(linear_search(numbers, 16))
# output: Target found