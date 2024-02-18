def bubble_sort(number):
    for i in range(len(number) - 1):
        is_changed = False
        for j in range(len(number) - 1 - i):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
                is_changed = True

        if not is_changed:
            break

    return number

# print(bubble_sort([2, 1, 4, 5, 3, 7, 1]))
# output: [1, 1, 2, 3, 4, 5, 7]