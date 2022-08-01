# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = {}
        p = head
        
        if p == None:
            return False
        
        while p.next != None:
            if p in count.keys():
                return True
            else:
                count[p] = 1
                p = p.next
            
        return False

