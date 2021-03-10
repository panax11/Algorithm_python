from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Too slow
def insertionSortList1(head: ListNode) -> ListNode:
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next

        cur = parent
    return cur.next


def insertionSortList2(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next

        if head and cur.val > head.val:
            cur = parent
    return parent.next