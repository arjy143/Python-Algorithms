def quicksort(numbers, low, high):
    if low < high:
        p = partition(numbers, low, high)
        quicksort(numbers, low, p-1)
        quicksort(numbers, p+1, high)
    return numbers

def partition(numbers, low, high):
    pivot = numbers[high]
    i = low-1
    for j in range(low, high-1):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

# numbers = [2, 1, 4, 5, 3, 7, 1]
# sorted_numbers = quicksort(numbers, 0, len(numbers)-1)
# print(sorted_numbers)
# output: [1, 1, 2, 3, 4, 5, 7]