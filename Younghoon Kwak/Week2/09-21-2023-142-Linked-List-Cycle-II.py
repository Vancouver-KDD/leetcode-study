# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Edge case 1: There is no cycle
        Edge case 2: How to break the loop when there's cycle
        How do you find there's a cycle?

        """
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                break
        else:
            return None  
          
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next        
        return slow
    
