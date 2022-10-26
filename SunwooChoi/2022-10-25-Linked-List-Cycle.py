# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check linked list has at least two nodes
        if not head or not head.next:
            return False
        
        # set two pointer which traverse linked list
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow pointer catches up fast pointer only if there is a cycle
            if slow == fast:
                return True
            
        return False

