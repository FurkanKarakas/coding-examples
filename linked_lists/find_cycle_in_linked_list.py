"""https://leetcode.com/problems/linked-list-cycle/

This is the illustration of the Floyd's cycle detection algorithm. Just make sure that both pointers start at head.
"""


class Node:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Node | None = None


def cycleInLinkedList(head: Node | None) -> Node | None:
    slow = fast = head
    while True:
        if not fast or not fast.next:
            # Reached the end of list. There are no cycles
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # A cycle has been found
            break

    # Determine the entry node to the cycle
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    head = Node(5)
    head.next = Node(6)
    head.next.next = Node(7)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(9)
    head.next.next.next.next.next = head.next.next  # Node(7)
    cycle_start = cycleInLinkedList(head)
    if cycle_start:
        print(f"There is a cycle in the linked list, and the cycle starts with the value: {
              cycle_start.val}")
    else:
        print("There are no cycles in the list.")
