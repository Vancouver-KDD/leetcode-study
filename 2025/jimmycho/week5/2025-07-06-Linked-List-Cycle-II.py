# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        slow_index = 0
        while fast and fast.next:
            slow_index += 1
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return
        start = head
        meet = slow
        while meet != start:
            meet = meet.next
            if meet == slow:
                start = start.next
        return start