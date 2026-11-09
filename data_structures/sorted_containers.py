"""
What are sorted containers?

Sorted containers are tree-based data structures that maintain their elements in a sorted order. They allow for efficient insertion, deletion, and lookup operations while ensuring that the elements remain sorted. Examples of sorted containers include:
* Sorted lists
* Sorted sets
* Sorted dictionaries

Sorted containers are implemented using balanced binary search trees, which provide logarithmic time complexity for insertion, deletion, and lookup operations.

These containers are useful in scenarios where you need to frequently access elements in a specific order or perform range queries.

Time complexities:
- Insertion: O(log n)
- Deletion: O(log n)
- Lookup: O(log n)
"""

from sortedcontainers import SortedList, SortedSet, SortedDict

if __name__ == "__main__":
    sortedList = SortedList([5, 1, 3, 2, 4])
    # Output: Sorted List: SortedList([1, 2, 3, 4, 5])
    print("Sorted List:", sortedList)
    # bisect_left: returns the leftmost index where the element can be inserted to maintain sorted order
    index = sortedList.bisect_left(3)
    # Output: Index of element 3 (bisect_left): 2
    print("Index of element 3 (bisect_left):", index)
    # bisect_right: returns the rightmost index where the element can be inserted to maintain sorted order
    index = sortedList.bisect_right(3)
    # Output: Index of element 3 (bisect_right): 3
    print("Index of element 3 (bisect_right):", index)
    sortedSet = SortedSet([1, 1, 2, 2, 3, 3])
    # Output: Sorted Set: SortedSet([1, 2, 3])
    print("Sorted Set:", sortedSet)
    sortedDict = SortedDict({'b': 3, 'a': 5, 'c': 1})
    # Output: Sorted Dict: SortedDict([('a', 5), ('b', 3), ('c', 1)])
    print("Sorted Dict:", sortedDict)
