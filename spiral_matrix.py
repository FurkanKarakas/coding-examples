"""
Given an m x n matrix, return all elements of the matrix in spiral order:

1 2 3
4 5 6
7 8 9

returns: 1 2 3 6 9 8 7 4 5
"""


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    rows_remaining = m
    cols_remaining = n
    arr = list()

    # We can keep moving right down left up as long as the remaining entities are greater than 1
    while rows_remaining > 1 and cols_remaining > 1:
        # Move right: 1 2 (1 fewer than the actual size)
        for j in range(cols_remaining-1):
            arr.append(matrix[i][j+i])
        # Move down: 3 6 (1 fewer than the actual size)
        for j in range(rows_remaining-1):
            arr.append(matrix[j+i][n-1-i])
        # Move left: 9 8 (1 fewer than the actual size)
        for j in range(cols_remaining-1):
            arr.append(matrix[m-1-i][n-1-i-j])
        # Move up: 7 4 (1 fewer than the actual size)
        for j in range(rows_remaining-1):
            arr.append(matrix[m-1-j-i][i])

        i += 1
        # There will be 2 fewer rows and columns in the inner frame in the next iteration
        rows_remaining -= 2
        cols_remaining -= 2

    if rows_remaining == 1 and cols_remaining == 1:
        # If there is only one item remaining, add it
        arr.append(matrix[i][i])
    elif rows_remaining == 1:
        # Else if there is just a row remaining, add the row by moving right
        for j in range(cols_remaining):
            arr.append(matrix[i][j+i])
    elif cols_remaining == 1:
        # Else if there is just a column remaining, add the column by moving down
        for j in range(rows_remaining):
            arr.append(matrix[j+i][n-1-i])

    return arr


if __name__ == "__main__":
    matrix = [
        [1, 2,  3,  4],
        [5, 6,  7,  8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    arr = spiralOrder(matrix)
    print(arr)
