def mergesort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        
        while i < len(left) and j < len(right):
                
                if left[i] <= right[j]:
                    numbers[k] = left[i]
                    i += 1
                else:
                    numbers[k] = right[j]
                    j += 1
                k += 1
                while i < len(left):
                    numbers[k] = left[i]
                    i += 1
                    k += 1
        
                while j < len(right):
                    numbers[k] = right[j]
                    j += 1
                    k += 1    

# numbers = [2, 3, 1, 5, 3]
# mergesort(numbers)
# print(numbers)
# output: [1, 2, 3, 3, 5]
