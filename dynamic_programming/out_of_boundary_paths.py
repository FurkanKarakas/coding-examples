"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 1e9 + 7.

Note that we can solve this problem with BFS, but it takes a lot of memory space (the queue gets too large).

We can also solve this problem with DFS, but it takes a lot of time and recursive callstack.

We will solve it with dynamic programming and storing the positions in the current and previous steps.
"""


def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    def is_inbound(x: int, y: int) -> bool:
        if x in (-1, m) or y in (-1, n):
            return False
        return True

    # dp stores the number of possible ways to reach that cell from previous move
    dp = [[0]*n for _ in range(m)]
    # Initialize it with 1 at the start position
    dp[startRow][startColumn] = 1
    result = 0
    # Store the directions the ball can move
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(maxMove):
        # Store the current configuration in a temporary matrix
        temp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # If there are no moves from the previous iteration, skip
                if dp[i][j] == 0:
                    continue

                # Move in each direction
                for direction_x, direction_y in directions:
                    x = i+direction_x
                    y = j+direction_y

                    if is_inbound(x, y):
                        # Add it to the possible moves from the previous iteration
                        temp[x][y] += dp[i][j]
                    else:
                        # Add it to the result, i.e., all of the possible moves from the previous iteration can go out of bound now.
                        result += dp[i][j]

        # Update dp with the current possible moves
        dp = temp

    return result % int(1e9 + 7)


if __name__ == "__main__":
    m, n, maxMove, startRow, startColumn = 5, 5, 3, 2, 2
    result = findPaths(m, n, maxMove, startRow, startColumn)
    print(result)
