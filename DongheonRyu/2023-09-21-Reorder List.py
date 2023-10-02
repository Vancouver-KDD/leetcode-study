class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find the middle value
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second linked list
        prev, current = None, slow.next
        slow.next = None  # 중간을 기준으로 연결을 끊음
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Combine two linked lists by zigzag
        first_half, second_half = head, prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
