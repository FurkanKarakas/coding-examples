def knapsack_backtracking(weights: list[float],
                          profits: list[float],
                          capacity: float) -> tuple[float, list[int]]:
    """This function solves 0/1 Knapsack Problem with non-integer weights
    using backtracking.

    Args:
        weights (list[float]): Weights of items
        profits (list[float]): Profits of items
        capacity (float): The maximum capacity of the bag

    Returns:
        tuple[float, list[int]]: The maximum profit and the indices of items
    """

    # Store the result as a dictionary
    result = {
        "max_profit": 0,
        "max_profit_indices": list()
    }

    def backtrack(current_indices: list[int],
                  current_profit: float,
                  current_weight: float,
                  remaining_indices: list[int]) -> None:

        if len(remaining_indices) == 0:
            if current_profit > result["max_profit"]:
                result["max_profit"] = max(
                    result["max_profit"], current_profit)
                result["max_profit_indices"] = current_indices
            return

        next_index = remaining_indices[0]
        next_weight = current_weight+weights[next_index]
        next_profit = current_profit+profits[next_index]

        if next_weight < capacity:
            backtrack(current_indices+[next_index],
                      next_profit,
                      next_weight,
                      remaining_indices[1:])
        elif next_weight > capacity:
            backtrack(current_indices,
                      current_profit,
                      current_weight,
                      remaining_indices[1:])
        else:
            if current_profit > result["max_profit"]:
                result["max_profit"] = max(
                    result["max_profit"], current_profit)
                result["max_profit_indices"] = current_indices

    backtrack(list(), 0, 0, [i for i in range(len(weights))])

    return (result["max_profit"], result["max_profit_indices"])


if __name__ == "__main__":
    weights = [1.2, 1.6, 2.6, 3.9, 4.0, 0.2]
    profits = [1.4, 1.8, 1.9, 2.2, 2.4, 1.0]
    capacity = 5.5
    max_profit, max_profit_indices = knapsack_backtracking(
        weights, profits, capacity)

    print(f"Max profit: {max_profit} Indices: {max_profit_indices}")
