# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        currNode = head
        length = 1

        while currNode.next:
            currNode = currNode.next
            length += 1

        k = k % length

        currNode.next = head

        temp = head
        # 1, 2, 3, 4, 5
        # 2
        # 5 - 2 = 3
        for _ in range(length - k - 1):
            temp = temp.next

        res = temp.next
        temp.next = None

        return res
