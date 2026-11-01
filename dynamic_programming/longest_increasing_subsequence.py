"""Given an array of integers, return the longest strictly increasing subsequence(s) and its length.
A subsequence is a subarray where elements appear in the same order. For example:

[1,5,2] is a subsequence of [0,1,6,5,4,3,2].

Let lis(i) be the longest increasing subsequence including the element nums[:i+1] ( i+1-th element). Then, we have the following substructure:

lis(i) = max(1, lis(j)+1) for all 0 <= j < i such that nums[i] > nums[j]

Then, the result is max(lis(k)) for k <= 0 <= len(nums)-1

Time complexity: O(n^2)
Worst case space complexity: O(n^2) ?
"""


def longest_increasing_subsequence(nums: list[int]) -> tuple[list[int], int]:
    # This list keeps track of the maximum elements coming before the current item at index i
    result_indices = [[] for _ in range(len(nums))]

    lis = [1]*len(nums)

    for i in range(1, len(lis)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j]+1)

        # Get all the indices which produce the maximum result
        for j in range(0, i):
            if nums[i] > nums[j]:
                if lis[j]+1 == lis[i]:
                    # This item is included in result of j
                    result_indices[i].append(j)

    # Construct the result
    result = max(lis)

    result_indexes = list()

    # Get all the indexes which produce the max result
    for i, item in enumerate(lis):
        if item == result:
            result_indexes.append(i)

    # Keep a stack for the depth-first search of the longest subsequences
    stack = list()

    # Keep all the solutions in this variable
    all_results = list()

    def generate_all_results(result_indexes: list[int]):
        if len(result_indexes) == 0:
            all_results.append(stack[::-1])
            return

        for index in result_indexes:
            stack.append(nums[index])
            generate_all_results(result_indices[index])
            stack.pop()

    generate_all_results(result_indexes)

    return all_results, result


if __name__ == "__main__":
    nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result_set, result = longest_increasing_subsequence(nums)
    print(f"The length of the longest increasing subsequence: {result}")
    for i, item in enumerate(result_set):
        print(f"Result number {i+1}: {item}")
