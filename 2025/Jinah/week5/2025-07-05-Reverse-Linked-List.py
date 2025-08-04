# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not head or not head.next:
            return head

        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        