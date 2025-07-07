# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        prev=head
        curr=head.next

        reverse_curr=None
        reverse_next = ListNode(prev.val, None)
        
        while curr.next:
            reverse_curr = ListNode(curr.val, reverse_next)
            # reverse_prev = ListNode(0, reverse_curr)
            # reverse_curr = reverse_prev
            reverse_next = reverse_curr
            prev=prev.next
            curr=curr.next 
        reverse_curr = ListNode(curr.val, reverse_next)

        return reverse_curr


            

        