# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous node
        prev = None
        
        while head:
            tmp = head.next # keep reference of next ListNode
            head.next = prev # reverse next reference
            prev = head
            head = tmp
            
        return prev

