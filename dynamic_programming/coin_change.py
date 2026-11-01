"""https://leetcode.com/problems/coin-change/description/

dp[i] = min dp[i-coin]+1 for all coin in coins

To reconstruct which coins we picked, we need to store the result in a separate list whenever we find a minimum.
"""


def coinChange(coins: list[int], amount: int) -> int:
    """
    dp[i] = min dp[i-coin]+1 for all coin in coins
    """

    if amount == 0:
        return 0

    dp = [0] * (amount+1)

    for i in range(1, amount+1):
        # Assign the result the highest value possible (+inf) and find the minimum among all coins.
        result = float("infinity")
        for coin in coins:
            # Out of bound
            if i-coin < 0:
                continue
            # Impossible state. We can't increment because there are no previous coins.
            if i-coin != 0 and dp[i-coin] == 0:
                continue
            result = min(result, dp[i-coin]+1)
        # If a minimum has been found, assign it to the dp
        if result != float("infinity"):
            dp[i] = result  # type: ignore
    return dp[amount] if dp[amount] != 0 else -1


if __name__ == "__main__":
    coins, amount = [25, 10, 50, 99], 1_500
    result = coinChange(coins, amount)
    print(result)
