class Node:
    def __init__(self, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value: int = value


def left_view(root: Node | None, current_height: int, max_height: list[int]) -> None:
    """Print the left view of a binary tree

    Args:
        root (Node): Root node
        current_height (int): Current height in the tree
    """

    if root is None:
        return

    if current_height == max_height[0]:
        max_height[0] += 1
        print(root.value)

    # Recursively trace the left and right subtrees. Note that left child is called first
    left_view(root.left, current_height+1, max_height)
    left_view(root.right, current_height+1, max_height)


if __name__ == "__main__":
    # height 0
    tree = Node(10)
    # height 1
    tree.left, tree.right = Node(6), Node(5)
    # height 2
    tree.left.right, tree.right.left, tree.right.right = Node(
        3), Node(7), Node(8)

    print(f"Left view of the tree:")
    left_view(tree, 0, [0])
