# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

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
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 5])
merged_list = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))
