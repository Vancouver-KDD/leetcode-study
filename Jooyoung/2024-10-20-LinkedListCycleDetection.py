# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def list_to_linked_list(items, index):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    cycle_node = None
    for i in range(1, len(items)):
        current.next = ListNode(items[i])
        current = current.next
        if i == index:
            cycle_node = current

    if index >= 0:
        current.next = cycle_node

    return head


solution = Solution()
linked_list = list_to_linked_list([1, 2, 3, 4], 1)
has_cycle = solution.hasCycle(linked_list)
print(has_cycle)
