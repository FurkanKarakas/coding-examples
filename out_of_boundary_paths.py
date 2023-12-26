"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 1e9 + 7.
"""

from collections import deque


def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    def cell_contribution(x: int, y: int) -> int:
        if x == y == 0 and m == n == 1:
            return 4
        if (x in (0, m-1) and y in (0, n-1)) and 1 in (m, n):
            return 3
        if (x in (0, m-1) or y in (0, n-1)) and 1 in (m, n):
            return 2
        if x in (0, m-1) and y in (0, n-1):
            return 2
        if x in (0, m-1) or y in (0, n-1):
            return 1
        return 0

    # dp=[[0]*n for _ in range(m)]
    q = deque()
    q.append((startRow, startColumn))
    currentMove = 0
    result = 0

    while len(q) > 0:
        if currentMove >= maxMove:
            break

        currentMove += 1
        qLen = len(q)
        # print(qLen)
        for i in range(qLen):
            x, y = q.popleft()
            result += cell_contribution(x, y)
            # Add up to queue
            if x-1 >= 0:
                q.append((x-1, y))
            # Add down to queue
            if x+1 <= m-1:
                q.append((x+1, y))
            # Add left to queue
            if y-1 >= 0:
                q.append((x, y-1))
            # Add right to queue
            if y+1 <= n-1:
                q.append((x, y+1))

    return result % int(1e9 + 7)


if __name__ == "__main__":
    m = n = 1
    maxMove = 4
    startRow = startColumn = 0
    result = findPaths(m, n, maxMove, startRow, startColumn)
    print(f"Result: {result}")
