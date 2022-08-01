# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remover(head):
            if not head:
                return 0, head

            i, head.next = remover(head.next)
            return i + 1, (head, head.next)[i + 1 == n]

        return remover(head)[1]