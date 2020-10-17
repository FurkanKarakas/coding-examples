from typing import List


def merge_sort(arr: List[int]):
    # Stop when the length of the array is 1, i.e., the array contains a single element.
    # This is our terminating criterion!
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr, L, R)


def merge(arr: List[int], L: List[int], R: List[int]):
    numelem_L = len(L)
    numelem_R = len(R)
    i = j = k = 0
    while i < numelem_L and j < numelem_R:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Remaining elements
    while i < numelem_L:
        arr[k] = L[i]
        k += 1
        i += 1

    while j < numelem_R:
        arr[k] = R[j]
        k += 1
        j += 1


if __name__ == '__main__':
    mylist = [8, 9, -1, 0, 5, 5, 2, 3, 5, 9, -40, 1, 0, 2]
    merge_sort(mylist)
    print(mylist)
