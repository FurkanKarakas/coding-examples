class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """This function computes the area of the largest rectangle in the given list.

        Algorithm:

        * Keep a stack which stores the tuple `(index,height)` with heights in increasing order
        * At the current element, pop the elements in the stack until you
          reach a short height. Update the index with the furthest 
          possible location that you could reach. 
          While popping, update the max area that you would have reached using that rectangle.
        * At the end, pop the remaining elements to calculate the maximum area.

        Args:
            heights (list[int]): Heights of the rectangles with width 1

        Returns:
            int: The maximum area of the rectangle in the given list
        """

        stack: list[tuple[int, int]] = list()
        max_area: int = -1
        for i, item in enumerate(heights):
            item_index = i
            while len(stack) > 0:
                last_index, last_height = stack[-1]
                if item > last_height:
                    break
                # If the last_height is gtoeq item, pop it and compute the area
                stack.pop()
                area = (i-last_index)*last_height
                max_area = max(max_area, area)
                # Set the item_index to last_index
                item_index = last_index
            stack.append((item_index, item))

        # At the end of iteration, compute the remaining elements
        while len(stack) > 0:
            i, item = stack.pop()
            max_area = max(max_area, (len(heights)-i)*item)

        return max_area


if __name__ == "__main__":
    heights = [1, 2, 3, 4, 3, 1]
    largest_area = Solution().largestRectangleArea(heights)
    print(f"The largest area of a rectangle in {heights} is: {largest_area}")
