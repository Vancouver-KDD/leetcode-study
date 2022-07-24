# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevNodes = {}
        
        
        def hasCycleInner(head):
            if head == None:
                return False

            if head in prevNodes:
                return True
            
            prevNodes[head] = True
            
            return hasCycleInner(head.next)
        
        return hasCycleInner(head)
        
