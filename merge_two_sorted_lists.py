"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    cur1, cur2 = list1, list2

    # If both lists are empty, return
    if not cur1 and not cur2:
        return None

    result = ListNode()
    cur = result
    # Compare each current list entry and add the smaller one to the cur
    while cur1 and cur2:
        if cur1.val < cur2.val:
            cur.val = cur1.val
            cur1 = cur1.next
        else:
            cur.val = cur2.val
            cur2 = cur2.next
        # If there are new entries remaining, create a new node
        if cur1 or cur2:
            cur.next = ListNode()
            cur = cur.next

    # Handle the remaining elements
    while cur1:
        cur.val = cur1.val
        cur1 = cur1.next
        # If there are new entries remaining, create a new node
        if cur1:
            cur.next = ListNode()
            cur = cur.next
    while cur2:
        cur.val = cur2.val
        cur2 = cur2.next
        # If there are new entries remaining, create a new node
        if cur2:
            cur.next = ListNode()
            cur = cur.next

    return result


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)

    list3 = mergeTwoLists(list1, list2)

    def print_linked_list(list: ListNode | None) -> None:
        if not list:
            return
        print(list.val)
        print_linked_list(list.next)

    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
    print("Merged list:")
    print_linked_list(list3)
