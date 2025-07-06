# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head

        while curr:
            next_node = curr.next      # Save next node
            curr.next = previous       # Reverse the link
            previous = curr            # Move previous forward
            curr = next_node           # Move curr forward

        return previous  # New head of the reversed list
