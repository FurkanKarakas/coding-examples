"""https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

We will solve this problem by using backtracking:

* At each index i, we have len(s)-i choices to partition the string.
* We make sure that the current partition forms a valid palindrome. If it does, then we move to the next iteration.

Time complexity: O(2^n * n^2) where n = len(s)
Explanation:
* In the base case, we are copying the stack, which takes n steps.
* We can partition a string of length n in 2^(n-1) ways. We can either put a separator in spaces (total n-1 spaces) between characters or not (2 choices).
* We need to check that the partition is a valid palindrome. For that, we need to do at most n // 2 comparisons.
* Result = n * 2^(n-1) * n // 2 = O(2^n * n^2)

Space complexity: O(2^n * n)
Explanation:
* We can have at most 2^(n-1) partitions.
* Each partition contains n characters (the size of the string).
* Result = 2^(n-1) * n = O(2^n * n)
"""


def partition(s: str) -> list[list[str]]:
    result = list()
    stack = list()

    def backtrack(i: int) -> None:
        if i == len(s):
            result.append(stack.copy())
            return

        newPartition = list()
        # We can partition this string anywhere from i to len(s)-1
        for x in range(i, len(s)):
            newPartition.append(s[x])
            isPalindrome = True
            # We need to make sure that this partition forms a valid palindrome
            for j in range(len(newPartition) // 2):
                if newPartition[j] != newPartition[len(newPartition)-1-j]:
                    # This isn't a valid palindrome. We skip this partition
                    isPalindrome = False
                    break
            # Now, this is a valid palindrome
            if isPalindrome:
                stack.append("".join(newPartition))
                backtrack(x+1)
                stack.pop()  # Backtrack: pop and process the next candidate

    backtrack(0)
    return result


if __name__ == "__main__":
    s = "aabcba"
    result = partition(s)
    for res in result:
        print(res)
