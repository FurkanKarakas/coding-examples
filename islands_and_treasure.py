"""https://neetcode.io/problems/islands-and-treasure

You are given a m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

This is a shortest path graph problem: Apply BFS for shortest path problems. ✅
"""

from collections import deque


def islandsAndTreasure(grid: list[list[int]]) -> None:
    ROWS = len(grid)
    COLS = len(grid[0])
    # INF = 2 ** 31 - 1
    directions = ((-1, 0), (+1, 0), (0, -1), (0, +1))
    q = deque()
    visited = set()
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 0:
                q.append((i, j))

    stage = 0
    while q:
        qLen = len(q)
        # Pop all elements from the queue
        for _ in range(qLen):
            i, j = q.popleft()
            if (
                    not 0 <= i <= ROWS - 1
                    or not 0 <= j <= COLS - 1
                    or grid[i][j] == -1
                    or (i, j) in visited
            ):
                continue

            visited.add((i, j))

            grid[i][j] = min(grid[i][j], stage)

            for dir_x, dir_y in directions:
                next_x, next_y = dir_x + i, dir_y + j
                q.append((next_x, next_y))

        stage += 1


if __name__ == "__main__":
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]

    islandsAndTreasure(grid)

    for row in grid:
        print(row)

    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]

    assert expected == grid
