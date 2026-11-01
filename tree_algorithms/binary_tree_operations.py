from treelib import Tree


class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val: int = val
        self.left: Node | None = left
        self.right: Node | None = right


class BinaryTree:
    def __init__(self, root: Node | None = None) -> None:
        self.root = root

    def insertKey(self, val: int) -> None:
        def insert_into_binary_tree(root: Node | None, val: int) -> Node | None:
            if root is None:
                return Node(val)

            if val > root.val:
                root.right = insert_into_binary_tree(root.right, val)
            elif val < root.val:
                root.left = insert_into_binary_tree(root.left, val)
            else:
                print("Duplicates not allowed!")

            return root

        self.root = insert_into_binary_tree(self.root, val)

    def deleteKey(self, val: int) -> None:
        def find_min(node: Node) -> Node:
            temp = node.right
            assert temp
            while temp and temp.left:
                temp = temp.left
            return temp

        def delete_node(root: Node | None, val: int) -> Node | None:
            # Base case
            if root is None:
                return root
            # Recursive call to move right to find the value
            if val > root.val:
                root.right = delete_node(root.right, val)
                return root
            if val < root.val:
                root.left = delete_node(root.left, val)
                return root

            # We found the item!
            # Case 1: It doesn't have any children
            if not root.left and not root.right:
                del root
                return None
            # Case 2: It has only one child
            if not root.left:
                temp = root.right
                del root
                return temp
            if not root.right:
                temp = root.left
                del root
                return temp
            # Case 3: It has both children
            temp = find_min(root)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)
            return root

        self.root = delete_node(self.root, val)

    def treeVisualization(self) -> None:
        treeViz = Tree()

        if self.root is not None:
            treeViz.create_node(self.root.val, "root")

        def printTree(root: Node | None, id: str) -> None:
            if root is None:
                return

            if root.left is not None:
                treeViz.create_node(root.left.val, id+".left", parent=id)
                printTree(root.left, id+".left")

            if root.right is not None:
                treeViz.create_node(root.right.val, id+".right", parent=id)
                printTree(root.right, id+".right")

        printTree(self.root, "root")

        viz = treeViz.show(stdout=False)
        print(viz)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insertKey(5)
    tree.insertKey(11)
    tree.insertKey(15)
    tree.insertKey(12)
    tree.insertKey(1)
    tree.insertKey(2)
    tree.insertKey(14)
    tree.insertKey(16)
    tree.insertKey(0)
    tree.insertKey(10)
    tree.insertKey(9)
    print(f"Before deleting the key 5:")
    tree.treeVisualization()
    tree.deleteKey(5)
    print(f"After deleting the key 5:")
    tree.treeVisualization()
