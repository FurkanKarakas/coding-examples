"""https://leetcode.com/problems/generate-parentheses/description/

Time complexity: O(N * 2**N) where N = 2*n

We have 2*n = N spots to fill (n opening and n closing parantheses). At each spot, we can make two decisions -> 2**N total cases
At each base case, we copy N characters to the result set. The cost of each base case is -> N
In total -> N * 2**N

Space complexity: O(n) for stack and recursive callstack
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """This function generates all valid parantheses of number of pairs n and returns the result.

        Args:
            n (int): The number of pairs of parantheses

        Returns:
            list[str]: The list which contains all possible solutions
        """

        # Mutable object, we can append the results
        result = list()
        # Mutable object, we can append the parantheses
        # This follows a depth-first approach since we are using a stack
        stack = list()

        # Define the function here to reduce the function call overhead
        def backTrack(openN: int, closeN: int) -> None:
            # Our base condition. Get the result in the stack and append it to the results
            if openN == closeN == n:
                result.append("".join(stack))
                return
            # If number of open parantheses is less than n, we can add more open parantheses
            if openN < n:
                stack.append("(")
                backTrack(openN+1, closeN)
                stack.pop()
            # If number of close parantheses is less than openN, we can add more close parantheses
            if closeN < openN:
                stack.append(")")
                backTrack(openN, closeN+1)
                stack.pop()

        backTrack(0, 0)

        return result


if __name__ == "__main__":
    results = Solution().generateParenthesis(5)
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")

    # See the number of possible parantheses pairs with various n
    for n in range(1, 16):
        num = len(Solution().generateParenthesis(n))
        print(f"n = {n}, num = {num}")
