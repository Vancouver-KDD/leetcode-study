# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = cur = ListNode()
        carry = 0
        
        while l1 and l2:
            curVal = l1.val + l2.val + carry
            carry = curVal // 10
            curVal = curVal % 10
            cur.val = curVal
            
            l1 = l1.next
            l2 = l2.next
            
            if carry == 0 and not l1 and not l2:
                return res
            
            
            nextNode = ListNode()
            cur.next = nextNode
            cur = cur.next
            
            
        if not l1 and not l2:
            if carry != 0:
                nextNode = ListNode()
                cur.next = nextNode
                cur = cur.next
                cur.val = carry
            return res
    
        leftover = l1 or l2
        
        while leftover:
            curVal = leftover.val + carry
            carry = curVal // 10
            curVal = curVal % 10
            cur.val = curVal
            
            if carry == 0 and not leftover.next:
                break
            
            nextNode = ListNode()
            cur.next = nextNode
            cur = cur.next
            
            leftover = leftover.next
            if not leftover and carry != 0:
                cur.val = carry
                
        return res
        
        
            
                    
        
        