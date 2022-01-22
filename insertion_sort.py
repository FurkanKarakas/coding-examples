from typing import List


def insertion_sort(arr: List[int]):
    """Insertion sort algorithm implemented in Python. Run time: O(n^2)

    Args:
        arr (List[int]): Array to be sorted
    """
    size = len(arr)
    for i in range(1, size):
        current = arr[i]
        j = i-1
        # Shift all elements to the right that are greater than the current
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current


if __name__ == "__main__":
    arr = [2, 3, -5, 6, 1, 0, 9, 7, 15, 6, 4, 3, 2, 1, 67, 8, 6, 5, 7, 5, 3]
    insertion_sort(arr)
    print(arr)
