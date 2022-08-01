# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            second = head
            first = head.next

            while second is not first:
                second = second.next
                first = first.next.next

            return True
        except:
            return False