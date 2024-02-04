"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

We can solve this problem by applying breath-first and setting all 1's to 0's, and incrementing the counter by 1.

We can also solve this problem by using depth-first search as well by using recursion. Maybe the recursive call stacks will be a lot in this case.
"""

from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        directions = ((-1, 0), (+1, 0), (0, -1), (0, +1))

        def bfs(i: int, j: int) -> None:
            q = deque([(i, j)])
            while q:
                cur_i, cur_j = q.popleft()
                if (
                    not 0 <= cur_i <= m - 1
                    or not 0 <= cur_j <= n - 1
                    or grid[cur_i][cur_j] != "1"
                ):
                    continue
                # Can also set it to 0. A special placeholder for the processed item
                grid[cur_i][cur_j] = "#"
                for dir_x, dir_y in directions:
                    q.append((cur_i + dir_x, cur_j + dir_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count


if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "0"],
        ["0", "1", "0", "1"],
        ["1", "0", "1", "0"],
        ["0", "1", "0", "1"]
    ]

    result = Solution().numIslands(grid)
    print(result)
