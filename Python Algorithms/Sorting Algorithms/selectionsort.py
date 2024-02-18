def selection_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

# numbers = [2, 1, 4, 5, 3, 7, 1]
# sorted_numbers = selection_sort(numbers)
# print(sorted_numbers)
# output: [1, 1, 2, 3, 4, 5, 7]
