def get_fibonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return get_fibonacci(index-1) + get_fibonacci(index-2)
    
# print(get_fibonacci(7))
# output: 13
