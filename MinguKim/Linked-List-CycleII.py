# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            print(current.val)
            if hasattr(current,'flag') and current.flag == 1:
                return current
            
            setattr(current, 'flag', 1)
            current = current.next
        return None
        
