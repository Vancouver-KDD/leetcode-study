"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: Iterative - O(n)
    def reverseList(self, head: ListNode) -> ListNode or None:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # Solution 2: Recursive
    def reverseList_recursive(self, head: ListNode) -> ListNode or None:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList_recursive(head.next)
            head.next.next = head
        head.next = None

        return newHead

    # Solution 3: Recursive 2
    def reverseList_recursive_2(self, head):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)
        return reverse(head, None)