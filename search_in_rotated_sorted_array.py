"""https://leetcode.com/problems/search-in-rotated-sorted-array/

We need to decide which half to visit. Note that at each iteration, at least one half will always be sorted.

* Case 1: Left half is sorted
  * Case 1.1: Target lies in this sorted half -> Go left
  * Case 1.2: Target doesn't lie in this sorted half -> Go right
* Case 2: Right half is sorted
  * Case 2.1: Target lies in this sorted half -> Go right
  * Case 2.2: Target doesn't lie in this sorted half -> Go left
"""


def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start+end)//2
        num_start, num_mid, num_end = nums[start], nums[mid], nums[end]
        if target == num_start:
            return start
        if target == num_mid:
            return mid
        if target == num_end:
            return end
        # Case 1: Left half is sorted
        if num_start < num_mid:
            # Case 1.1: Target lies in this sorted half
            if num_start < target < num_mid:
                # Continue left
                end = mid-1
            # Case 1.2: Target doesn't lie in this sorted half
            else:
                # Continue right
                start = mid+1
        # Case 2: right half is sorted (num_mid < num_end)
        else:
            # Case 2.1: Target lies in this sorted half
            if num_mid < target < num_end:
                # Continue right
                start = mid+1
            # Case 2.2: Target doesn't lie in this sorted half
            else:
                # Continue left
                end = mid-1

    return -1


if __name__ == "__main__":
    nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    result = search(nums, target)
    print(result)
