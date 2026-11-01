"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

Useful methods from the Python package heapq:

* heapify(arr): convert the list into a minHeap in-place where arr[i] <= arr[2*i+1] and arr[2*i+2] for all i. arr[0] will be the smallest element.
* heappush(arr, val): push the val to the heap and preserve the minHeap structure.
* heappop(arr): pop the smallest element from the heap and preserve the minHeap structure.
* heappushpop(arr, val): first push, then pop from the heap, preserving the minHeap structure.
* heapreplace(arr, val): first pop, then push to the heap, preserving the minHeap structure.

The last two operations are more efficient than calling heappush and heappop successively.
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Use a min heap to get the minimum element in O(1) time
        self.heap = nums
        heapq.heapify(self.heap)
        # Pop from the heap until the number of elements is exactly k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # If the heap isn't of size k, push to the heap and return
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        # If value is ltoet the min value, return min value
        # In this case, val can never be the k-th largest element
        # since the k-th largest element is the smallest element in the heap (at index 0)
        if val <= self.heap[0]:
            return self.heap[0]
        # Else, pop the min value and add the new value
        # heapreplace: first pop, then push
        # heappushpop: first push, then pop
        heapq.heapreplace(self.heap, val)
        return self.heap[0]


if __name__ == "__main__":
    program = KthLargest(3, [4, 5, 8, 2])
    print(program.add(3))
    print(program.add(5))
    print(program.add(10))
    print(program.add(9))
    print(program.add(4))
