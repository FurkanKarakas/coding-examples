"""https://leetcode.com/problems/subsets-ii/description/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

We will solve this problem using backtracking.

At each index, we can take two decisions:

* Decision 1: Include the number in the subset.
* Decision 2: Don't include the number in the subset. In this case, skip all repeating subsequent numbers.

Note that the number of unique subsets are the product of all frequencies + 1:

* If the frequency of an item is x, it has x+1 choices: include 0 of it, 1 of it, 2 of it, ..., x of it -> x+1 choices
* The number of unique subsets is the product of all these frequencies plus 1.
"""


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    result = list()
    stack = list()
    nums.sort()

    def backtrack(i: int) -> None:
        if i == len(nums):
            result.append(stack.copy())
            return
        # Decision 1: Include the number in the subset
        stack.append(nums[i])
        backtrack(i+1)
        stack.pop()
        # Decision 2: Don't include the number in the subset
        # In this case, skip all subsequent numbers
        i += 1
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1
        backtrack(i)

    backtrack(0)
    return result


if __name__ == "__main__":
    nums = [0, 0, 1, 1]
    result = subsetsWithDup(nums)
    for subset in result:
        print(subset)
