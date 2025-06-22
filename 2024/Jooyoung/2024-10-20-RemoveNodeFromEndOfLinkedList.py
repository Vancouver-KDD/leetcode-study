# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


def list_to_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linked_list_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


solution = Solution()
linked_list = list_to_linked_list([1, 2, 3, 4])
result_list = solution.removeNthFromEnd(linked_list, 2)
print(linked_list_to_list(result_list))
