class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # swap the values

        first = second = head

        for _ in range(k-1):
            first = first.next

        tail = first

        while tail.next:
            second = second.next
            tail = tail.next

        first.val, second.val = second.val, first.val
        return head
