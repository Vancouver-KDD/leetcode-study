# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # No cycle
            return None

        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
