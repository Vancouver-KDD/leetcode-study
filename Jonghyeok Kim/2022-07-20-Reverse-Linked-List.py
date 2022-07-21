
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur, nex = None, head, None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            if nex is None:
                return cur
            cur = nex