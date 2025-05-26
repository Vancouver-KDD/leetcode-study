# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate over the linkedlist and swap first/second
        new_head = ListNode()
        new_head.next = head
        prev = new_head

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = prev.next.next

        return new_head.next

        # Time complexity: O(n)
        # Space complexity: O(1)