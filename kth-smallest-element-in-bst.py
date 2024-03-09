"""https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1198891100/

We will solve this problem using in-order traversal of the BST.

We will use the iterative approach using a stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: TreeNode | None, k: int) -> int:
    # We need to do in-order traversal of the binary tree and get the k-th element
    stack = list()
    cur = root
    n = 0
    while cur or stack:
        # Go all the way left
        # While doing so, add the nodes to the stack
        while cur:
            stack.append(cur)
            cur = cur.left
        # We reached to the end of the left traversal
        if stack:
            n += 1
            cur = stack.pop()
            # If we are at the k-th element, return it
            if n == k:
                return cur.val
            # Otherwise, continue with the right subtree
            cur = cur.right
    return -1


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)  # This one is the 3-rd smallest
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(kthSmallest(root, 3))
