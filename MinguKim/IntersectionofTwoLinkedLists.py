# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #precalculus method and below
        currentA = headA
        currentB = headB
        while currentA != currentB:
            
            if currentA == None:
                currentA = headB
            else:
                currentA = currentA.next

            if currentB == None:
                currentB = headA
            else:
                currentB = currentB.next
            
        return currentB

        
