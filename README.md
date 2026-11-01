# Some Random Coding Examples, Mainly Implemented in Python

Trying to write some basic algorithms in the programming language Python, mostly taken from the websites `LeetCode` and `HackerRank`.

## Organization

Python examples are grouped by their primary problem-solving approach:

- `arrays_and_strings/`: array, string, matrix, and two-pointer problems.
- `backtracking/`: recursive search through combinations and choices.
- `data_structures/`: implementations and problems centered on heaps, stacks, queues, and caches.
- `dynamic_programming/`: problems solved with overlapping subproblems and stored results.
- `graph_algorithms/`: graph traversal, shortest paths, spanning trees, and disjoint sets.
- `greedy/`: problems solved by making locally optimal choices.
- `linked_lists/`: linked-list algorithms.
- `math_and_bit_manipulation/`: numerical and bitwise algorithms.
- `sorting_and_searching/`: sorting and search algorithms.
- `tree_algorithms/`: binary tree construction, traversal, and properties.

## Some Problems and the Corresponding Video Explanations

- [Minimum Size Subarray Sum](https://www.youtube.com/watch?v=aYqYMIqZx5s): The idea is to reduce the extra computations that we do if we investigate every start and end points (That would have been $O(n^2)$ in time complexity). If we include an element by extending the end point to the right and the current sum exceeds the target value, then this means that we can start searching for a smaller window by moving the start pointer to the right (there can be no subarray between start+1 and previous end since the new extended end is the first time we exceed the target).
