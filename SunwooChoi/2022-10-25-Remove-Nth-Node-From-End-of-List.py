# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.getSize(head, 0)
        # if size is 1, delete one and return empty list
        if size == 1:
            return None
        
        # target is the nth element from beginning
        target = size - n - 1
        cur = head
        
        # if target is in the middle of list
        if target >= 0:
            while target > 0:
                cur = cur.next
                target -= 1
            cur.next =cur.next.next
            return head
        
        # if taget == -1, then delete the first node
        return head.next
    
    # get total number of nodes in the list
    def getSize(self, head: Optional[ListNode], cur: int) -> int:
        if not head:
            return cur
        return self.getSize(head.next, cur+1)

