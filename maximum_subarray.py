from typing import List, Tuple


def kadene_algorithm(arr: List[int]) -> Tuple[int, int, int]:
    """This function implements the Kadene's algorithm which finds the maximum subarray of a given array.

    Args:
        arr (List[int]): This is a list of positive and negative integers. At least one integer must be non-negative.

    Returns:
        Tuple[int, int, int]: Returns the largest sum, start index of the subarray and the end index of the subarray inclusive.
    """

    # current_sum variable stores the sum ending in index i and starting in a non-negative sum index (start_index_temp).
    # best_sum variable stores the best sum seen so far.
    start_index_temp = start_index = end_index = best_sum = current_sum = 0
    for i, x in enumerate(arr):
        current_sum = current_sum+x
        # If current_sum is negative, reset the potential start index.
        # We basically go bankrupt: start from a potentially new start index :)
        if current_sum < 0:
            current_sum = 0
            # The next index after the current index that we are at.
            start_index_temp = i+1
        if best_sum >= current_sum:
            pass
        # Adapt the new suggested starting index from the current sum and the last index
        else:
            best_sum = current_sum
            end_index = i
            start_index = start_index_temp
    return best_sum, start_index, end_index


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    best_sum, start_index, end_index = kadene_algorithm(arr)
    print(f"Array: {arr}", f"Best sum: {best_sum}", f"Start index: {start_index}",
          f"End index: {end_index}", f"Maximum subarray: {arr[start_index:end_index+1]}", sep="\n")
