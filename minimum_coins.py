"""Given an array of coins with integer values and a target sum, return 
the minimum number of coins and each coin's count to obtain the target money.

This problem can be solved using Dynamic Programming by observing the following optimal substructure:

minCoin(target) = min(minCoin(target - coins[i])) + 1 where 0 <= i <= len(coins)-1

We basically try all the solutions and pick up the one that yields the minimum result.

Important: Assume that a solution exists.
"""


def minCoin(coins: list[int], target: int) -> tuple[int, dict[int, int]]:
    result_dict = dict()

    dp = [0]*(target+1)
    result_coins = [0]*(target+1)

    for i in range(1, len(dp)):
        minItem = float("inf")
        for coin in coins:
            j = i-coin
            if j < 0:
                # Invalid result. The current target sum is exceeded
                continue

            result = dp[j]

            if result < minItem:
                minItem = result
                # Store the coin
                result_coins[i] = coin

        dp[i] = minItem+1  # type: ignore

    # Construct the result
    current = target
    while current > 0:
        coin_value = result_coins[current]

        result_dict[coin_value] = result_dict.get(coin_value, 0)+1
        current -= coin_value

    return dp[target], result_dict


if __name__ == "__main__":
    coins_ = [10, 5, 4]
    target_ = 32

    result, result_coins = minCoin(coins_, target_)

    print(f"Minimum number of coins: {result}")
    for key, value in result_coins.items():
        print(f"  Coin: {key} Count: {value}")
