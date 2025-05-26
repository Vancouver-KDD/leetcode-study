# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


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
linked_list = list_to_linked_list([0, 1, 2, 3])
reversed_list = solution.reverseList(linked_list)
print(linked_list_to_list(reversed_list))
