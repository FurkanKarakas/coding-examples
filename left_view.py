class Node:
    def __init__(self, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value: int = value


def tree_height(root: Node | None) -> int:
    """Calculate the height of the tree whose root is `root`
    """

    if root is None:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))


def left_view(root: Node | None, current_height: int, height_dict: dict[str, int]) -> None:
    """Print the left view of a binary tree

    Args:
        root (Node): Root node
        current_height (int): Current height in the tree
        height_dict (dict): Dictionary storing "height" and "last_height"
    """

    if root is None:
        return
    # If the last printed height is "gtoet" height of tree, simply return
    if height_dict["last_height"] >= height_dict["height"]:
        return
    # We have the desired element here
    if current_height > height_dict["last_height"]:
        height_dict["last_height"] += 1
        print(root.value)
    # Recursively trace the left and right subtrees. Note that left child is called first
    left_view(root.left, current_height+1, height_dict)
    left_view(root.right, current_height+1, height_dict)


if __name__ == "__main__":
    # height 0
    tree = Node(10)
    # height 1
    tree.left, tree.right = Node(6), Node(5)
    # height 2
    tree.left.right, tree.right.left, tree.right.right = Node(
        3), Node(7), Node(8)
    height = tree_height(tree)
    d = dict({"last_height": -1,
              "height": height})
    print(f"The height of the tree: {height}")
    print(f"Left view of the tree:")
    left_view(tree, 0, d)
