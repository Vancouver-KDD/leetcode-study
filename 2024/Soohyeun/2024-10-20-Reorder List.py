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
        # use stack
        temp = head
        node_stack = []
        list_len = 0
        while temp:
            node_stack.append(temp)
            temp = temp.next
            list_len += 1

        new_head = ListNode()
        curr = new_head
        temp = head
        half = list_len //2
        while half:
            curr.next = temp
            temp = temp.next
            curr.next.next = node_stack.pop()
            curr = curr.next.next
            half -= 1

        if list_len % 2 != 0:
            curr.next = temp
            curr = curr.next
        curr.next = None
        return new_head.next