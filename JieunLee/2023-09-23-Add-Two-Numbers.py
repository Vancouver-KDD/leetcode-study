# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        pt1, pt2 = l1, l2
        dummy_head = ListNode(0)
        pt = dummy_head

        while pt1 or pt2 or carry:
            x = pt1.val if pt1 else 0
            y = pt2.val if pt2 else 0
            sum = carry + x + y
            
            carry = sum // 10
            sum = sum % 10 
            pt.next = ListNode(sum)
            pt = pt.next

            pt1 = pt1.next if pt1 else None
            pt2 = pt2.next if pt2 else None

        return dummy_head.next