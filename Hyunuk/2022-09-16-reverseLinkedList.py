# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr, next_ = None, head, head.next
        while curr:
            curr.next, prev, curr = prev, curr, next_
            next_ = next_.next if next_ else None
        return prev
