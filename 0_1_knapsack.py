"""Given N items where each item has some weight and profit associated with it 
and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. 
The task is to put the items into the bag such that the sum of profits associated 
with them is the maximum possible. 

Note: The constraint here is we can either put an item completely into the bag 
or cannot put it at all [It is not possible to put a part of an item into the bag].

This problem is a maximization problem, a maximization problem is an optimization problem. 
We can generally solve optimization problems by dynamic programming if we can 
find an optimal substructure in the given problem.

Let knapsack(n, capacity) be the maximum profit that we can get using first n items 
and with the total weight 'capacity'. Then, we have the following substructure:

knapsack(n, capacity) = max(knapsack(n-1, capacity), 
                            knapsack(n-1, capacity-weights[n-1]) + profits[n-1])

I.e., to the optimal result, we can either include the item n or not include it. 
The first argument of max function is the scenario where we don't include it. 
The second argument of max function is the scenario where we include it. 
Simply take the maximum of these two to find the result.
"""


from datetime import datetime


def zero_one_knapsack(weights: list[int], profits: list[int], capacity: int) -> tuple[list[int], int]:
    result_indices = [0]*len(weights)

    # Result is knapsack[len(weights)][capacity]
    knapsack = [[0]*(capacity+1) for _ in range(len(weights)+1)]
    knapsack_result = [[False]*(capacity+1) for _ in range(len(weights)+1)]

    for i in range(len(weights)+1):
        for j in range(capacity+1):
            if i-1 < 0:
                item1 = 0
            else:
                item1 = knapsack[i-1][j]
            if i-1 < 0 or j-weights[i-1] < 0:
                item2 = 0
            else:
                item2 = knapsack[i-1][j-weights[i-1]]+profits[i-1]

            knapsack[i][j] = max(item1, item2)

            if item2 > item1:
                # Item i was included in the optimal set with capacity j
                knapsack_result[i][j] = True

    # Reconstruct the solution
    max_profit = knapsack[-1][-1]
    i = len(weights)
    j = capacity

    while max_profit > 0:
        item_included = knapsack_result[i][j]
        if item_included:
            result_indices[i-1] = 1
            max_profit -= profits[i-1]
            j -= weights[i-1]
        i -= 1

    return result_indices, knapsack[-1][-1]


if __name__ == "__main__":
    weights_ = [1, 3, 5, 7]
    profits_ = [2, 4, 7, 10]
    capacity_ = 8

    t1 = datetime.now()
    result_indices_, max_profit_ = zero_one_knapsack(
        weights_, profits_, capacity_)
    t2 = datetime.now()

    print(f"Result indices: {result_indices_}\nMax profit: {max_profit_}")
    print(f"Time taken: {(t2-t1).microseconds//1000} ms")
