"""https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Let dp[i] denote the result of the word break of the string starting at index 0. Then:

dp[i] = OR dp[i+len(word)] for word in wordDict

OR here represents the logical OR operator.

The base case is dp[len(s)] = True (empty string).
"""


def wordBreak(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s)+1)
    # Base case
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for word in wordDict:
            wordLen = len(word)
            # Out of bound
            if i+wordLen > len(s):
                continue
            if word == s[i:i+wordLen] and dp[i+wordLen]:
                dp[i] = True
                break
    return dp[0]


if __name__ == "__main__":
    s, wordDict = "leetcode", ["leet", "code"]
    result = wordBreak(s, wordDict)
    print(result)
