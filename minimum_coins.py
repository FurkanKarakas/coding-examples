"""Given an array of coins with integer values and a target sum, return 
the minimum number of coins and each coin's count to obtain the target money.

This problem can be solved using Dynamic Programming by observing the following optimal substructure:

minCoin(target) = min(minCoin(target - coins[i])) + 1 where 0 <= i <= len(coins)-1

We basically try all the solutions and pick up the one that yields the minimum result.
"""

import time


def minCoinTopDown(coins: list[int], target: int) -> float:
    """Using memoization. Use DP instead"""
    memo = dict()

    def dfs(i):
        if i < 0:
            return float("inf")
        if i == 0:
            return 0
        if i in memo:
            return memo[i]
        result = min([dfs(i-coin) for coin in coins])+1
        memo[i] = result
        return memo[i]

    return dfs(target)


def minCoin(coins: list[int], target: int) -> tuple[float, dict[int, int]]:
    result_dict = dict()

    dp = [float("inf")]*(target+1)
    dp[0] = 0
    result_coins = [0]*(target+1)

    for i in range(1, target+1):
        for coin in coins:
            j = i-coin
            if j < 0:
                # Invalid result. The current target sum is exceeded
                continue

            result = dp[j]

            if result < dp[i]:
                dp[i] = result
                # Store the coin
                result_coins[i] = coin

        dp[i] += 1

    # Construct the result
    if dp[target] == float("inf"):
        # Result not found
        return -1, dict()

    current = target
    while current > 0:
        coin_value = result_coins[current]

        result_dict[coin_value] = result_dict.get(coin_value, 0)+1
        current -= coin_value

    return dp[target], result_dict


if __name__ == "__main__":
    coins_ = [1, 2, 5, 7, 10, 20, 22, 23, 25, 29, 45]
    target_ = 1_500

    result, result_coins = minCoin(coins_, target_)

    print(f"Minimum number of coins: {result}")
    for key, value in result_coins.items():
        print(f"  Coin: {key} Count: {value}")
