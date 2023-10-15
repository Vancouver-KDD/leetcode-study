#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        dummy=ListNode(0)
        dummy.next=head

        prev=dummy
        cur=dummy.next

        for i in range(1,left):
            cur=cur.next
            prev=prev.next

        for i in range(right-left):
            temp=cur.next
            cur.next=temp.next
            temp.next=prev.next
            prev.next=temp    

        return dummy.next
