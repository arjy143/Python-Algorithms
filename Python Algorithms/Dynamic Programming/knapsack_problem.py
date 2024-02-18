def find_best_combination(n,w,profit,weight):
    if n == 0 or w == 0:
        return 0
    if (weight[n - 1] > w):
        return find_best_combination(n-1, w, profit, weight)
    else:
        return max(profit[n - 1] + find_best_combination( n - 1, w - weight[n - 1], profit, weight),
                    find_best_combination(n-1, w, profit, weight))

# profit = [60, 100, 120]
# weight = [10, 20, 30]
# w = 50
# n = len(profit)
# print(find_best_combination(n,w,profit,weight))
# output: 220