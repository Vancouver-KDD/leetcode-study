# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge two halfs
        fir, sec = head, prev
        while sec:
            temp1, temp2 = fir.next, sec.next
            fir.next = sec
            sec.next = temp1
            fir, sec = temp1, temp2