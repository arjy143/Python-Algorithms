def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

# numbers = [2, 1, 4, 5, 3, 7, 1]
# sorted_numbers = insertion_sort(numbers)
# print(sorted_numbers)
# output: [1, 1, 2, 3, 4, 5, 7]