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
        
        length = 0
        node = head
        
        while node:
            node = node.next
            length += 1
        
            
        
            
        
        
        
    