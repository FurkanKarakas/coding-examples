"""
https://leetcode.com/problems/remove-covered-intervals/description/

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
Return the number of remaining intervals.
"""


def removeCoveredIntervals(intervals: list[list[int]]) -> int:
    """
    Similar to any interval problems, we want to read the events in a timeline, so we first arrange the intervals by their starting position.
    However, we have one additional objective:
    * Every interval that can cover another interval should appear earlier.
    * Therefore, when two intervals start at the same position, the longer interval must come first.
    In that case, we sort by the ending position in descending order.
    Time Complexity: O(nlog n) due to sorting
    """
    intervals.sort(key=lambda x: (x[0], -x[1]))  # O(nlog n)
    maxEndSoFar = intervals[0][1]
    n = len(intervals)
    result = n
    for i in range(1, n):  # O(n)
        start, end = intervals[i]
        if end <= maxEndSoFar:
            result -= 1
        maxEndSoFar = max(maxEndSoFar, end)
    return result


if __name__ == "__main__":
    intervals = [[1, 4], [3, 6], [2, 8]]
    print(removeCoveredIntervals(intervals))  # Output: 2
    intervals = [[1, 4], [2, 3]]
    print(removeCoveredIntervals(intervals))  # Output: 1
