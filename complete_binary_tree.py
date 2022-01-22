class Node:
    def __init__(self) -> None:
        """Initialize a node in the binary tree
        """

        self.left = None
        self.right = None


def count_number(node: Node) -> int:
    """Returns the number of nodes in a binary tree

    Args:
        node (Node): Root of the binary tree

    Returns:
        int: Number of nodes in the binary tree whose root is `node`
    """

    if node is None:
        return 0
    return 1 + count_number(node.left) + count_number(node.right)


def is_complete(node: Node, index: int, number_nodes: int) -> bool:
    """Returns a boolean whether the binary tree is complete.
    If the binary tree is not complete, then there will be some gaps in the array representation of the array.
    E.g.: Array: [4,2,6,x,1,2]
          Index: [0,1,2,3,4,5]
    Check if every index is greater than or equal to the number of nodes in the tree.
    If we find at least one index (5 above) which is "gtoet" the number of nodes (5 above), then the tree is not complete.

    Args:
        node (Node): Root of the binary tree
        index (int): Current index in the array representation
        number_nodes (int): Number of nodes in the binary tree

    Returns:
        bool: Returns whether the binary tree is complete
    """

    if node is None:
        return True
    if index >= number_nodes:
        return False
    return (is_complete(node.left, 2*index+1, number_nodes) and is_complete(node.right, 2*index+2, number_nodes))


if __name__ == "__main__":
    # tree1 is a complete binary tree
    tree1 = Node()
    tree1.left = Node()
    tree1.right = Node()
    tree1.left.left = Node()
    num_nodes1 = count_number(tree1)
    tree1_is_complete = is_complete(tree1, 0, num_nodes1)
    print(f"Tree 1 is a complete binary tree: {tree1_is_complete}")

    # tree2 is NOT a complete binary tree
    tree2 = Node()
    tree2.left = Node()
    tree2.left.right = Node()
    num_nodes2 = count_number(tree2)
    tree2_is_complete = is_complete(tree2, 0, num_nodes2)
    print(f"Tree 2 is a complete binary tree: {tree2_is_complete}")
