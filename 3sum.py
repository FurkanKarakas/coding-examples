class Solution:
    """We need to find 3 numbers in the given array such that their sum adds up to zero.
    This is an extension to the 2sum problem and we can use the same 2 pointers 
    method to solve this problem. The result elements must be unique.

    It works as follows:

    * First, sort the given array.
    * Store the results as 3 numbers (a, b, c) such that a <= b <= c
    * While iterating for a, if you encounter the same element, simply skip it
      since all results are already found in the previous step.
    * While finding 2sum (b, c) for fixed a, if you find a solution
     (b, c) and encounter the same b, shift the index for b (which is j) 1 unit to right.
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # Stores integers in sorted order [a, b, c]
        result = list()
        a_values = set()
        for i, num in enumerate(nums[:-2]):
            # If num is already present in the result list, skip
            if num in a_values:
                continue
            a_values.add(num)
            # For each number, do two-pointer technique
            target = -num
            # Start j from i+1
            j = i+1
            k = len(nums)-1
            # If b appears in the result set, move j forward
            b_values = set()
            while j < k:
                if nums[j] in b_values:
                    j += 1
                    continue

                current = nums[j]+nums[k]
                if current == target:
                    b_values.add(nums[j])
                    result.append([num, nums[j], nums[k]])
                    # Continue with the search by moving j and k
                    j += 1
                    k -= 1
                elif current < target:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4, -5, 5, -2, 1]
    result = Solution().threeSum(nums)
    for i, item in enumerate(result):
        print(f"Result {i+1}: {item}")
