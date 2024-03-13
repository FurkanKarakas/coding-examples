"""https://leetcode.com/problems/permutations-ii/description/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

We will use backtracking to solve this problem.

* First, we will sort the input array.
* We will use a boolean array to keep track whether the num at index i is already used.
* If the number is already used, we will go to the next number.
* If the number isn't used and also its duplicate at previous index isn't used either, we will skip this number. 
First, we will make sure that the same number at earlier index is used not to do the same permutations twice.
"""


def permuteUnique(nums: list[int]) -> list[list[int]]:
    result = list()
    stack = list()
    nums.sort()
    used = [False] * len(nums)

    def backtrack():
        if len(stack) == len(nums):
            result.append(stack.copy())
            return
        for i in range(0, len(nums)):
            if used[i]:
                continue
            # If the previous one isn't used yet, don't use this one
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue
            used[i] = True
            stack.append(nums[i])
            backtrack()
            used[i] = False
            stack.pop()

    backtrack()
    return result


if __name__ == "__main__":
    permute_result = permuteUnique([1, 1, 2, 2])
    for i in permute_result:
        print(i)
