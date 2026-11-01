"""https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

We will solve this problem using backtracking. The trick is not to include any repeating consequtive numbers if we decide not to include this number.

Also, don't forget to sort the array at the start.
"""


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = list()
    stack = list()

    def backtrack(i: int, current: int) -> bool:
        if current == target:
            result.append(stack.copy())
            return False
        if (
            i == len(candidates) or
            current > target
        ):
            return False

        # Decision 1: Include this number
        stack.append(candidates[i])
        b = backtrack(i+1, current+candidates[i])
        # Decision 2: Don't include this number
        stack.pop()
        # Small optimization. If the target is already reached or exceeded, don't do any more forward search.
        if b:
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            backtrack(i, current)
        return True

    backtrack(0, 0)
    return result


if __name__ == "__main__":
    candidates, target = [2, 5, 2, 1, 2], 5
    result = combinationSum2(candidates, 5)
    for item in result:
        print(item)
