# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        curr = head
        ahead = head
        for _ in range(n):
            ahead = ahead.next

        if not ahead:
            return head.next

        while ahead:
            ahead = ahead.next
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head