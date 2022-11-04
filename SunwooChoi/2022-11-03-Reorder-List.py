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
        if not head:
            return head
        
        # find the spliting point
        middle = self.findMiddle(head)
        # reverse right side of linked list
        right = self.reverse(middle.next)
        # delete reference from last node in node
        middle.next = None
        left = head
        
        # reorder linked list
        while left and right:
            tmp_left = left.next
            tmp_right = right.next
            left.next = right
            right.next = tmp_left
            left = tmp_left
            right = tmp_right
                
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, slow, fast =None, head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


