# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = l3 = ListNode(-1)
        carry = 0
        while l1 or l2:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            carry, sum_ = divmod(l1_val + l2_val + carry, 10)
            l3.next = ListNode(sum_)
            l3 = l3.next
        if carry:
            l3.next = ListNode(carry)
            l3 = l3.next
            
        return dummy.next
    
    
    
"""
2 4 3
  ^

5 6 4
  ^

-1
^
"""
