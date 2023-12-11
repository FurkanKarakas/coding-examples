"""This example shows the template for a binary search algorithm. Return the index of the searched element if it exists, otherwise return -1.

For a binary search to be applicable, there are some conditions:

1. The array must be sorted.
2. The elements of the array must have an ordering relation (< > ==).

By assigning start and end to mid+1 and mid-1 respectively, we will eventually get out of the while loop.
"""


def binary_search(arr: list[int], target: int) -> int:
    """arr is an array in non-descending order
    """
    # Start is the first index
    start = 0
    # End is the last index
    end = len(arr)-1

    # Loop as long as start <= end (both indices are included in our search)
    # In a Pythonic way, it would have been arr[start:end+1]

    while start <= end:
        # Take the mid as the mid point between start and end
        # If start+end is odd, then mid will be closer to start
        # Note that mid will never be equal to end, but it might be equal to start if end == start+1
        # If you need to compare mid with the end points, do the comparison with end instead of start because of this reason
        mid = (start+end)//2

        # In this case, we have found our item
        if arr[mid] == target:
            return mid

        # In this case, continue with the search on the left
        if target < arr[mid]:
            end = mid-1
        # In this case, continue with the seach on the right
        else:
            start = mid+1

    # If the search was unsuccessful, return -1
    return -1


if __name__ == "__main__":
    arr_ = [0, 1, 1, 1, 2, 3, 4, 5, 9, 11, 19, 25, 30, 32, 32, 40, 55]
    target_ = 40

    index = binary_search(arr_, target_)

    print(f"Item is at index: {index}")
