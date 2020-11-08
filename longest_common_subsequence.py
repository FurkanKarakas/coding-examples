# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""Dynamic programming method: note that s1[i]==s2[j] implies LCS[i,j] = 1+LCS[i-1,j-1]. Else, LCS[i,j] = max(LCS[i-1,j],LCS[i,j-1])
The table is being filled from top to bottom. The answer (the longest common substring) is being read from bottom to top.
The length of the longest common substring is the most south-east element in the table.
    """


def LCS(s1, s2):
    # Initialization
    m = len(s1)
    n = len(s2)
    A = [[0]*(n+1) for _ in range(m+1)]
    # Filling the table from top to bottom
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                A[i][j] = A[i-1][j-1]+1
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])
    # Backtracking and finding a solution from bottom to top
    i, j = m, n
    lcs = ""
    while i != 0 and j != 0:
        if A[i][j] == A[i-1][j]:
            i -= 1
        elif A[i][j] == A[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            lcs = s1[i]+lcs
    return lcs, A[-1][-1]


if __name__ == "__main__":
    s1 = "ABCDEF"
    s2 = "FBDAMN"
    lcs, size = LCS(s1, s2)
    print(
        f"The longest common substring of {s1} and {s2} is {lcs} and it is of size {size}.")
