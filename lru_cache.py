"""https://leetcode.com/problems/lru-cache/description/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
"""


class Node:
    def __init__(self, key=-1, prev=None, next_=None):
        self.key: int = key
        self.prev: Node | None = prev
        self.next: Node | None = next_


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeToTail(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def evictNode(self) -> Node:
        return self.removeNode(self.head.next)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.linkedList = LinkedList()

    def get(self, key: int) -> int:
        if key in self.dict:
            val, nodeRef = self.dict[key]
            self.linkedList.removeNode(nodeRef)
            self.linkedList.addNodeToTail(nodeRef)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key][0] = value
            nodeRef = self.dict[key][1]
            self.linkedList.removeNode(nodeRef)
            self.linkedList.addNodeToTail(nodeRef)
            return
        if len(self.dict) == self.capacity:
            evictedNode = self.linkedList.evictNode()
            evictedKey = evictedNode.key
            del self.dict[evictedKey]
        newNode = Node(key)
        self.dict[key] = [value, newNode]
        self.linkedList.addNodeToTail(newNode)


if __name__ == "__main__":
    capacity = 3
    obj = LRUCache(capacity)
    param_1 = obj.get(1)
    print(param_1)
    obj.put(1, 1)
    param_1 = obj.get(1)
    obj.put(2, 2)
    obj.put(3, 3)
    obj.put(4, 4)
    param_1 = obj.get(1)
    print(param_1)
    param_1 = obj.get(2)
    print(param_1)
