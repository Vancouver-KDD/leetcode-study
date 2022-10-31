# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check empty lists
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        head1, head2 = list1, list2
        
        if head1.val < head2.val:
            res = cur = head1
            head1 = head1.next
        else:
            res = cur = head2
            head2 = head2.next
            
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        
        if head1 == None:
            cur.next = head2
        if head2 == None:
            cur.next = head1

        
        return res
