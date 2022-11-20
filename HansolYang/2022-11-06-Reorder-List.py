# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        
        def get_mid(node):
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next 
            if p2.next:
                p2 = p2.next
            return p1, p2
        
        def reverse(m):
            p = m.next
            prev = m
            while p.next:
                temp = p.next
                p.next = prev
                p, prev = temp, p
            p.next = prev
            m.next = None
        
        def reorder(p1, p2):
            while p1:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2
            
        
        mid, tail = get_mid(head)
        
        reverse(mid) #reverse mid ~ tail
        temp = tail
        h = head
        
        reorder(h, tail)
        
        return head