"""https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Observe the following patterns:

* Let's say we have heights 5 and 4. Notice that 5 can't be extended to the right since 4 is blocking it.
* We will use this principle and remove the items from the stack if the top of the stack contains taller heights than the current one.
* Once the current item is the tallest one at the top of the stack, we push this height to the stack.
* As the starting index, we don't give the index of the height in the array, but we give the index until which previous index the current height could be extended.
* Also, whenever you pop from the stack, make sure to update the maximum area accordingly.
* If there are no more heights to be processed, we process the remaining heights in the stack.
"""


def largestRectangleArea(heights: list[int]) -> int:
    stack = list()
    max_area = 0

    for i, height in enumerate(heights):
        starting_index = i
        while stack:
            last_height, last_index = stack[-1]
            if last_height > height:
                starting_index = last_index
                stack.pop()
                max_area = max(max_area, (i-last_index)*last_height)
            else:
                break
        stack.append((height, starting_index))

    # Process the remaining heights in the stack
    while stack:
        height, index = stack.pop()
        max_area = max(max_area, (len(heights)-index)*last_height)

    return max_area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    max_area = largestRectangleArea(heights)
    print(max_area)
