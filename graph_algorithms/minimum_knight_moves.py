"""https://leetcode.ca/all/1197.html

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

We solve this problem by BFS.
"""

from collections import deque


def minimum_moves(start_position: tuple[int, int], end_position: tuple[int, int]) -> int:
    current_time = 0
    visited: set[tuple[int, int]] = set()
    directions = (
        (+1, +2),
        (+2, +1),
        (+2, -1),
        (+1, -2),
        (-1, -2),
        (-2, -1),
        (-2, +1),
        (-1, +2)
    )
    q = deque([start_position])
    while q:
        found = False
        qLen = len(q)
        for _ in range(qLen):
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == end_position:
                found = True
                break
            for i, j in directions:
                next_x, next_y = i+x, j+y
                q.append((next_x, next_y))
        if found:
            break
        current_time += 1
    return current_time


if __name__ == "__main__":
    start_position = (0, 0)
    end_position = (100, 100)
    result = minimum_moves(start_position, end_position)
    print(result)
