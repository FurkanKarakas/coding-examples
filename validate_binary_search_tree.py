"""https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode | None) -> bool:
    # We will pass min_val and max_val to each iteration
    # This will specify the range that the node value must be inside
    # If it doesn't satisfy this constraint, it can't be a BST
    # Time: O(n)
    # Space: O(H) where H = height of the tree due to recursive call stack
    def dfs(node, min_val, max_val):
        if not node:
            return True
        if not min_val <= node.val <= max_val:
            return False
        # For left recursion, the max value can be node.val-1
        # For right recursion, the min value can be node.val+1
        return dfs(node.left, min_val, node.val-1) and dfs(node.right, node.val+1, max_val)

    return dfs(root, -float("inf"), float("inf"))
