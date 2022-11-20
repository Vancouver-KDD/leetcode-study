# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        curr = dummy
        for _ in range(size - n):
            curr = curr.next
        curr.next = curr.next.next if curr else None
        return dummy.next
