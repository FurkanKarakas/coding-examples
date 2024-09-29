"""https://leetcode.com/problems/all-oone-data-structure/description/?envType=daily-question&envId=2024-09-29

All O`one Data Structure

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.

* inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
* dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
* getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
* getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.

We will solve this problem by combining a dictionary with a doubly linked list:

* The dictionary will map the string to a node.
* The linked list will contain nodes with increasing count from left to right.
"""


class Node:
    def __init__(self, prev=None, next=None, count=0.0, val=""):
        self.prev: Node | None = prev
        self.next: Node | None = next
        self.val = val
        self.count = count


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(count=float("-infinity"))
        self.tail = Node(count=float("infinity"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, newNode: Node) -> None:
        self.head.next, newNode.next = newNode, self.head.next
        newNode.prev = self.head
        assert newNode.next
        newNode.next.prev = newNode

    def removeNode(self) -> None:
        assert self.head.next
        self.head.next = self.head.next.next
        assert self.head.next
        self.head.next.prev = self.head

    def swapWithNextNode(self, node: Node) -> None:
        # Store the node pointers
        a = node.prev
        assert a
        assert node.next
        assert node.next.next
        node2 = node.next
        b = node.next.next
        # Make the changes
        node.next = b
        node.prev = node2
        node2.next = node
        node2.prev = a
        a.next = node2
        b.prev = node

    def siftRight(self, node: Node) -> None:
        assert node.next
        while node.count > node.next.count:
            self.swapWithNextNode(node)

    def siftLeft(self, node: Node) -> None:
        assert node.prev
        while node.count < node.prev.count:
            self.swapWithNextNode(node.prev)


class AllOne:
    def __init__(self):
        self.countDict: dict[str, Node] = dict()
        self.ll = DoublyLinkedList()

    def inc(self, key: str) -> None:
        if key not in self.countDict:
            newNode = Node()
            newNode.val = key
            newNode.count = 1
            self.ll.insertNode(newNode)
            self.countDict[key] = newNode
            return
        self.countDict[key].count += 1
        self.ll.siftRight(self.countDict[key])

    def dec(self, key: str) -> None:
        self.countDict[key].count -= 1
        self.ll.siftLeft(self.countDict[key])
        if self.countDict[key].count == 0:
            self.ll.removeNode()
            del self.countDict[key]

    def getMaxKey(self) -> str:
        assert self.ll.tail.prev
        return self.ll.tail.prev.val

    def getMinKey(self) -> str:
        assert self.ll.head.next
        return self.ll.head.next.val


if __name__ == "__main__":
    print("Running the test for the class `AllOne`")
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    assert obj.getMaxKey() == "hello"
    assert obj.getMinKey() == "hello"
    obj.inc("leet")
    assert obj.getMaxKey() == "hello"
    assert obj.getMinKey() == "leet"
    print("Successfully passed the test!")
