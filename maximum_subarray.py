"""https://leetcode.com/problems/maximum-subarray/description/


Given an array of integers, return the maximum subarray sum, start and end indices.

We can solve this problem using dynamic programming by observing the following substructure:

dp[i] = max(dp[i-1]+arr[i], arr[i])

We can optimize the dynamic programming approach by just taking the previous item in the dp array.
"""


def maximum_subarray(arr: list[int]) -> tuple[int, int, int]:
    result = -abs(arr[0])-1
    dp_prev = -abs(arr[0])-1
    start = 0
    end = 0

    for i, item in enumerate(arr):
        temp1 = dp_prev+item
        temp2 = max(temp1, item, result)

        if temp2 == temp1:
            # Adopt the previous start index
            end = i
        elif temp2 == item:
            # Both indices start here
            start = end = i
        else:
            # Maximum element didn't change, don't change
            pass

        dp_prev = max(temp1, item)
        result = temp2

    return result, start, end


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    result, start, end = maximum_subarray(arr)
    print(f"Array: {arr}\nMaximum subarray sum: {
          result}\nStart index: {start}\nEnd index: {end}")
