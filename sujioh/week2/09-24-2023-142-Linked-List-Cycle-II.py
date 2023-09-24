# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        # detect cycle
        while fast.next and fast:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


'''
Summary
1. The "fast" pointer moves two steps at a time, and the "slow" pointer moves one step at a time 
    to detect the presence of a cycle within the list.
2. When a cycle is detected (the "fast" and "slow" pointers meet), 
    the "fast" pointer is reset to the head of the list, 
        and both pointers move one step at a time until they meet again. 
        The meeting point is the starting node of the cycle.
3. If there is no cycle (the "fast" pointer or its next node becomes None), 
    the algorithm returns None to indicate no cycle is present.


Confused
1. After they meet inside the cycle initially, 
    one pointer goes back to the head, and the other stays inside. 
    Moving together helps find where they diverged, the starting node.

2. initial detection is not starting point 
'''
