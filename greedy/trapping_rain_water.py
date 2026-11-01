"""https://leetcode.com/problems/trapping-rain-water/

Note that for an index i, the rain water that we can be trapped is min(maxL, maxR) - height[i] if > 0, else 0.
maxL and maxR are the maximum heights left and right to the index.
What we can do is we can keep track of maxL and maxR seen so far and two pointers i and j.
We move the pointer that has less maxL or maxR.
"""


def trap(height: list[int]) -> int:
    result = 0
    maxL = maxR = 0
    i, j = 0, len(height)-1
    while i <= j:
        if maxL <= maxR:
            result += max(min(maxL, maxR) - height[i], 0)
            maxL = max(maxL, height[i])
            i += 1
        else:
            result += max(min(maxL, maxR) - height[j], 0)
            maxR = max(maxR, height[j])
            j -= 1
    return result


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    print(trap(height))
