# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to solve, we can use two pointers, "previous" and "current"
        # we can start by initializing the "previous" as Null (in Python None) and "current" as the current head
        # then, follow these four steps:
        # 1. save the next node (current.next) to a temp or dummy node
        # 2. reverse the link: "current" node now points towards "previous" node
        # 3. shift the pointers
        # 4. repeat while nodes are not Null
        # we want to return "previous" at the end as "previous" will be the last item to be added, hence the new head

        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous
