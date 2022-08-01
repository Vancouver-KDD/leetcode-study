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
#         1. Divide the list into two halves
#         2. reverse the second half
#         3. alternately merge two lists 
        
        
        # Get the node in the middle of the list
        mid = end = head
        while (end.next != None and end.next.next != None):
            mid = mid.next
            end = end.next.next
        
        # Reverse the second half
        def reverseList(h):
            if h == None or h.next == None:
                return h    
            newHead = reverseList(h.next)
            h.next.next = h
            h.next = None
            return newHead

        headTwo = reverseList(mid)
        
        res = head
        nextOne = head.next
        nextTwo = headTwo.next
        # Alternate merge of two lists
        while(head != None and headTwo != None):
            head.next = headTwo
            headTwo.next = nextOne
            head = nextOne
            headTwo = nextTwo
            if nextOne != None and nextTwo != None:
                nextOne = nextOne.next
                nextTwo = nextTwo.next
        
        return res
        
        
            
            
            
        
        
        
    