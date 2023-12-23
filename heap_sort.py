"""Given an array of integers, sort them using a max heap data structure.

Note that a heap is a complete binary tree.

In an array representation of a heap:
- The parent node index is: (i-1) // 2
- The left child index is: 2*i + 1
- The right child index is: 2*i + 2

First, we will need to build the heap. We will use heapify method which 
sifts the elements downwards and we will traverse the array backwards.

The same operation can also be done by sifting the elements upwards 
(as if we are inserting a new element to the heap) while 
traversing the array forwards, but this takes O(n*log n) time as opposed to the previous method 
which takes O(n) time. There is a mathematical proof that the former operation takes O(n) time.

Next, we will pop elements one by one from the root, and put the last element to the root. 
Then we will heapify the array to construct the heap again.
"""


def heap_sort(arr: list[int]) -> None:
    def heapify(i: int, n: int) -> None:
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
            heapify(largest, n)

    # Build the heap by traversing the array backwards
    # We can start with the index (n-2)//2 = n//2 - 1 (the parent of the last item)
    # Since the leaf nodes don't have any children
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(i, n)

    # One by one, swap root with the last element
    # Reduce the heap size by 1
    # And do heapify for the new root element
    # The last element in the loop will already be sorted at index 0, don't include it in the loop
    for i in range(n-1, 0, -1):
        # Swap root with last
        arr[i], arr[0] = arr[0], arr[i]
        # Do the heapify to the root element with the reduced heap size
        heapify(0, i)


if __name__ == "__main__":
    arr = [5, 8, 1, 10, 20, 30, 22, 7, 0, -1, -4, 18]
    heap_sort(arr)
    print(arr)
