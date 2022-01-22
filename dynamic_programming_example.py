# Find the total number of paths from start to end
# - - - x
# x - - -
# - x - -
# - x - -
# Start: (0,0)
# End: (3,3)

def countPaths(start, end, grid, paths):
    """This function uses recursion with memoization (top-down). This has a disadvantage of additional callstack against tabulation (bottom-up approach).

    Args:
        start (tuple): Start of path
        end (tuple): end of path
        grid (list): N-by-N grid which shows blocks
        paths (dict): Dictionary used for memoization

    Returns:
        int: Possible number of paths from start to end
    """
    if start == end:
        return 1
    if start[0] >= len(grid) or start[1] >= len(grid) or not grid[start[0]][start[1]]:
        return 0
    rightSquare = (start[0], start[1]+1)
    downSquare = (start[0]+1, start[1])
    # Populating the dictionary here
    if rightSquare not in paths:
        paths[rightSquare] = countPaths(rightSquare, end, grid, paths)
    if downSquare not in paths:
        paths[downSquare] = countPaths(downSquare, end, grid, paths)
    if start not in paths:
        paths[start] = paths[rightSquare]+paths[downSquare]
    return paths[start]


if __name__ == "__main__":
    start = (0, 0)
    end = (3, 3)
    grid = [
        [True, True, True, False],
        [False, True, True, True],
        [True, False, True, True],
        [True, False, True, True]
    ]
    paths = dict()
    count = countPaths(start, end, grid, paths)
    print(f"The total number of paths: {count}")
