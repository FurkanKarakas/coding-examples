"""https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/description/

You are given an array nums consisting of non-negative integers.

We define the score of subarray nums[l..r] such that l <= r as nums[l] AND nums[l + 1] AND ... AND nums[r] where AND is the bitwise AND operation.

Consider splitting the array into one or more subarrays such that the following conditions are satisfied:

* Each element of the array belongs to exactly one subarray.
* The sum of scores of the subarrays is the minimum possible.

Return the maximum number of subarrays in a split that satisfies the conditions above.

A subarray is a contiguous part of an array.

Notes:

Let res = num1 AND num2.
Then res AND num3 can be at most res if num3 matches res's 1 bits at every location.
Hence adding a number to AND operator will make the result smaller or equal.
Conversely, removing a number will make the result greater or equal.
"""

from functools import reduce


def maxSubarrays(nums: list[int]) -> int:
    minScore = reduce(lambda num1, num2: num1 & num2, nums)
    # If minScore isn't 0 then we can only form a single subarray which is the array itself
    # Proof: let res = a AND b AND c AND d
    # res1 = a AND b >= res, res2 = b AND c >= res, res1 + res2 >= 2 * res > res
    if minScore != 0:
        return 1
    # 1 2 3 4 -> 001 010 011 100
    currentScore = None
    result = 0
    for num in nums:
        if currentScore is None:
            currentScore = num
        currentScore &= num
        if currentScore == 0:
            result += 1
            currentScore = None
    return result


if __name__ == "__main__":
    nums = [1, 0, 2, 0, 1, 2]
    # Subarrays: (1,0); (2,0); (1,2)
    print(maxSubarrays(nums))
    nums = [1, 0, 2, 0, 1, 3]
    # Subarrays: (1,0); (2,0,1,3)
    print(maxSubarrays(nums))
