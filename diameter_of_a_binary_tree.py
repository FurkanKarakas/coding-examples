"""https://leetcode.com/problems/diameter-of-binary-tree/description/
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode | None) -> int:
    # Map each node to its height
    node_height_dict: dict[TreeNode | None, int] = dict()

    def dfs(node: TreeNode | None) -> int:
        if node is None:
            return -1
        # Current node height is 1 + maximum node height of left and right subtrees
        node_height_dict[node] = 1+max(dfs(node.left), dfs(node.right))
        return node_height_dict[node]

    dfs(root)

    node_height_dict[None] = -1
    max_diam: list[int] = [0]

    # The diameter associated with a node is 2+height_left+height_right
    # Calculate the diameter for each node, and take the maximum one
    def dfs_diam(node: TreeNode | None) -> None:
        if node is None:
            return
        max_diam[0] = max(
            max_diam[0],
            2+node_height_dict[node.left]+node_height_dict[node.right]
        )
        dfs_diam(node.left)
        dfs_diam(node.right)

    dfs_diam(root)

    return max_diam[0]
