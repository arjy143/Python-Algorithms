def coin_row_maximum(coin_row):
    coin_maximums = [None] * len(coin_row)
    coin_maximums[0] = 0
    coin_maximums[1] = coin_row[1]
    for i in range(2, len(coin_row)):
        coin_maximums[i] = max(coin_row[i] + coin_maximums[i-2], coin_maximums[i-1])
    return coin_maximums[len(coin_row) - 1]

# coin_row = [1,2,3,4,5,6]
# print(coin_row_maximum(coin_row))
# output: 12