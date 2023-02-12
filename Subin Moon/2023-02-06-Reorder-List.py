"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: Tortoise & Hare algorithm O(n)
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle point
        hare, tortoise = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        # Reverse second half
        second = tortoise.next
        prev = tortoise.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    # Solution 2: Using Queue
    def reorderList_Q(self, head):
        from collections import deque
        q = deque()
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy.next
        while cur:
            q.append(cur)
            cur = cur.next

        cur = dummy
        even = False
        while q:
            node = q.pop() if even else q.popleft()
            node.next = None
            cur.next = node
            cur = cur.next
            even ^= True
        return head
