"""Given an array of integers, implement the operations insert, delete, and build_heap.
"""


def heapify(arr: list[int], i: int, n: int) -> None:
    """Heapify method adjusts the element at index i in the heap of size n 
    so that the element goes to the correct location in the heap by sifting 
    the element downwards in the heap. This method will change the input array.

    Args:
        i (int): index of the element which we want to put to the correct place
        n (int): the size of the heap, i.e., the number of elements
    """

    # Get the indices of left and right chidren
    l, r = 2*i+1, 2*i+2
    # Assign the index of the largest element among root, left and right to root for now
    largest = i

    # Check that the left child is not out of bound and is larger than the item at i
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check that the right child is not out of bound and is larger than both root and left
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is different than i, do the swap with the root and recursively continue
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


def insert_into_heap(arr: list[int], item: int) -> None:
    def sift_upwards(i: int) -> None:
        parent = (i-1)//2
        if parent > 0 and arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            sift_upwards(parent)

    arr.append(item)
    sift_upwards(len(arr)-1)


def delete_from_heap(arr: list[int]) -> None:
    if len(arr) == 0:
        return

    arr[-1], arr[0] = arr[0], arr[-1]
    arr.pop(-1)
    heapify(arr, 0, len(arr))


def build_max_heap(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)


if __name__ == "__main__":
    arr = [5, 8, 1, 10, 20, 30, 22, 7, 0, -1, -4, 18]
    print(f"Input array: {arr}")
    build_max_heap(arr)
    print(f"Heap: {arr}")
    insert_into_heap(arr, 25)
    print(f"Inserted 25 into heap: {arr}")
    delete_from_heap(arr)
    print(f"Deleted the root from heap: {arr}")
