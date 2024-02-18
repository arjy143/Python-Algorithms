def get_fib_dynamic(index):
    store = [None] * (index)
    n1 = 0
    n2 = 1
    for i in range(index):
        store[i] = n2
        n2 += n1
        n1 = store[i]
    return store[len(store)-1]

# print(get_fib_dynamic(7))
# output: 13

        