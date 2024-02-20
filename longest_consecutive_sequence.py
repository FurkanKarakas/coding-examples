"""https://leetcode.com/problems/longest-consecutive-sequence/

Given an array of integers, return the length of the longest consecutive sequence in the array.

Example input: [100,4,200,1,3,2]
Example output: 4 (the longest consecutive sequence in this array is [1, 2, 3, 4])

We can solve this problem by converting the list into a set. Then, for each element in the set, find the starting point on the sequence.
If there is the number num-1 in the set, then num can't be the start of the sequence. Skip.
If there is no number num-1 in the set, then count all numbers that appear consecutively.

Time complexity: O(n) since we visit each number at most twice.
Space complexity: O(n) for the set.
"""

def longestConsecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    cur_max = 0
    for num in nums:
        prev_num = num-1
        if prev_num in nums_set:
            continue
        cur = num
        while cur in nums_set:
            cur += 1
        cur_max = max(cur_max, cur-num)
    return cur_max

if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))