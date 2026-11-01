def quick_sort(arr: list[int], start: int, end: int) -> None:
    """This function implements quick sort algorithm.

    Args:
        arr (list): list to be sorted
        start (int): start index of the list
        end (int): end index of the array
    """

    # Criterion for the recursive calls. If start >= end, then there is nothing to sort and simply finish the current call in the stack.
    if start < end:
        # q returns the index of the element which partitions the array.
        q = partition(arr, start, end)
        quick_sort(arr, start, q-1)
        quick_sort(arr, q+1, end)


def partition(arr: list[int], start: int, end: int) -> int:
    # print(arr, start, end)
    partitioning_element = arr[end]
    # The parameter i keeps track of the index of the large element
    # The smallest index where a larger element than the pivot element resides
    i = start

    # Do not count the last element (pivot) in the loop
    for j in range(start, end):
        # Deal with smaller elements
        if arr[j] < partitioning_element:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Last step to put the partitioning element between smaller and larger elements.
    arr[end] = arr[i]
    arr[i] = partitioning_element
    return i


if __name__ == '__main__':
    mylist = [2, 3, -5, 6, 1, 0, 9, 7, 15, 6, 4, 3, 2, 1, 67, 8, 6, 5, 7, 5, 3]
    quick_sort(mylist, start=0, end=len(mylist)-1)
    print(mylist)
