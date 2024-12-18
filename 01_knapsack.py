def knapsack(values, weights, capacity):
    n = len(values) 
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

values = [12, 10, 20, 15]
weights = [2, 1, 3, 2]
capacity = 5

max_value = knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
