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
        curr = head
        fast = head
        slow = head
        stack = []

        # slow node becomes the first node of second half
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        # Push second_half nodes to stack
        while slow:
            stack.append(slow)
            slow = slow.next

        # Modify linked list (pop node and put it in-place)
        while len(stack) != 0:
            put_node = stack.pop()
            put_node.next = curr.next
            curr.next = put_node
            curr = curr.next.next

        curr.next = None

        # time complexity = O(n/2) + O(n/2) + O(n/2) = O(n)
        # Space complexity = O(1)