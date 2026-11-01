"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

We will solve this problem by DFS and keeping track of the min and max elements encountered so far.

We need to reset the current min and max between left and right children (left and right have no ancestor relationship).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxAncestorDiff(root: TreeNode | None) -> int:
    max_val: list[float] = [0]
    cur_max_min = [(-float("inf"), float("inf"))]

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return
        cur_max, cur_min = cur_max_min[0]

        max_val[0] = max(max_val[0], cur_max-node.val)
        max_val[0] = max(max_val[0], node.val-cur_min)

        cur_max_min[0] = (max(cur_max, node.val), min(cur_min, node.val))
        dfs(node.left)
        cur_max_min[0] = (max(cur_max, node.val), min(cur_min, node.val))
        dfs(node.right)

    dfs(root)
    return int(max_val[0])
