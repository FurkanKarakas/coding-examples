"""https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

We notice the following: in a path, there can be at most one splitting node.
A splitting node in a path is a node which goes through the node's left and right children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode | None) -> int:
    result = [-float("inf")]

    def dfs(node: TreeNode | None) -> int:
        if not node:
            return 0
        # Calculate left and right subproblems
        left = dfs(node.left)
        right = dfs(node.right)
        # Update the result if we split at this node
        result[0] = max(
            result[0],
            node.val,
            node.val+left,
            node.val+right,
            node.val+left+right
        )
        # Return the non-splitting max
        return max(
            node.val,
            node.val+left,
            node.val+right
        )

    dfs(root)
    return int(result[0])
