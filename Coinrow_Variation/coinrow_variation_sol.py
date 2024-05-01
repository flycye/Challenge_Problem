def maxCoinValue(coins):
    n = len(coins)

    if n == 0: return 0
    if n == 1: return coins[0]

    maxValues = [0] * n
    maxValues[1] = max(coins[0], coins[1])

    for i in range(2, n):
        maxValues[i] = max(maxValues[i - 2] + coins[i], maxValues[i - 1])

    return maxValues[n - 1]

coins = [5, 1, 2, 10, 6, 2]
print("max coin value: ", maxCoinValue(coins))
