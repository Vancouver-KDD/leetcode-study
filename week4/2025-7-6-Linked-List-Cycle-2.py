# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                break

        print('here')
        if not p2 or not p2.next:
            return None

        p2 = head

        while p1 != p2:
            p2 = p2.next
            p1 = p1.next
            
        return p1