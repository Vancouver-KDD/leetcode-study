# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                ptr1 = head
                ptr2 = slow
                while ptr1 is not ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1
        return None
