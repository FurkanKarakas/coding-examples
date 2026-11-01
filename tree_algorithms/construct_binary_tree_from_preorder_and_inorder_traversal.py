"""
First, note that preorder[0] is always the root.
Let index = inorder.index(preorder[0]). Note that everything before index (not included) in Inorder
is in the left subtree, and everything after index (not included) in Inorder is in the right subtree.

Preorder:
print(root) # 1 element at 0
print(root.left) # x or "index"-many elements at [1:index+1]
print(root.right) # y elements at [index+1:]

Inorder:
print(root.left) # x or "index"-many elements at [0:index]
print(root) # 1 element at index
print(root.right) # y elements at [index+1:]
"""
from treelib import Node, Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    root = TreeNode(preorder[0])

    index = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:index+1], inorder[:index])
    root.right = buildTree(preorder[index+1:], inorder[index+1:])

    return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    tree = buildTree(preorder, inorder)
    treeViz = Tree()

    if tree is not None:
        treeViz.create_node(tree.val, "root")

    def printTree(root: TreeNode | None, id: str) -> None:
        if root is None:
            return

        if root.left is not None:
            treeViz.create_node(root.left.val, id+".left", parent=id)
            printTree(root.left, id+".left")

        if root.right is not None:
            treeViz.create_node(root.right.val, id+".right", parent=id)
            printTree(root.right, id+".right")

    printTree(tree, "root")

    viz = treeViz.show(stdout=False)
    print(viz)
