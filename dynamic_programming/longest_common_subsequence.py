# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""Dynamic programming method: note that s1[i]==s2[j] implies LCS[i,j] = 1+LCS[i+1,j+1]. Else, LCS[i,j] = max(LCS[i+1,j],LCS[i,j+1])
The length of the longest common substring is the integer at index (0,0).

LCS[i,j] denotes the length of the longest common subsequence of the strings s1[i:] and s2[j:]
(only considering the strings after i and j characters, respectively)
"""


import datetime


def LCS(s1, s2):
    # Initialization
    m = len(s1)
    n = len(s2)
    A = [[0]*(n+1) for _ in range(m+1)]

    # i tracks the index for s1
    for i in range(m-1, -1, -1):
        # j tracks the index for s2
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                A[i][j] = A[i+1][j+1]+1
            else:
                A[i][j] = max(A[i][j+1], A[i+1][j])

    # Construct the result by reading the table entries
    result = ""
    i = j = 0
    while A[i][j] != 0:
        if A[i+1][j+1]+1 == A[i][j]:
            result += s2[j]
            i += 1
        j += 1

    return result, A[0][0]


if __name__ == "__main__":
    s1 = "ABCDEF"
    s2 = "FBDAMN"
    t1 = datetime.datetime.now()
    lcs, size = LCS(s1, s2)
    t2 = datetime.datetime.now()
    print(
        f"The longest common substring of {s1} and {s2} is {lcs} and it is of size {size}.")
    print(f"Time taken: {(t2-t1).microseconds//1e3} ms")
