"""
Given two strings str1 and str2, return the length of the longest common substring.

First, we will solve the longest common prefix problem:

lcp(i, j) = lcp(i+1, j+1) if str[i] == str[j], else 0

The indexes i and j represent the strings str1[i:] and str2[j:], respectively.

Then, we find the result of the original problem by finding the max for all pairs of lcp.
"""


def longestCommonSubstring(str1: str, str2: str) -> int:
    memo = dict()
    n1, n2 = len(str1), len(str2)

    def longestCommonPrefix(i: int, j: int) -> int:
        if i == n1 or j == n2:
            return 0
        if str1[i] != str2[j]:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = 1 + longestCommonPrefix(i+1, j+1)
        return memo[(i, j)]

    result = 0
    for i in range(n1):
        for j in range(n2):
            result = max(result, longestCommonPrefix(i, j))
    return result


if __name__ == "__main__":
    str1 = "aaaaabcdezzzz"
    str2 = "kkkkabcdllll"
    print(longestCommonSubstring(str1, str2))
