# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two Pointers
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nAhead = nBehind = head
        
        for _ in range(n):
            nAhead = nAhead.next
        
        if nAhead == None:
            return head.next
        
        
        while(nAhead.next != None):
            nAhead = nAhead.next
            nBehind = nBehind.next
        
        nBehind.next = nBehind.next.next
        return head
        
class Solution:
    
    #Brute Force? 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        m = 0
        dummy = dummyTwo = head
        while(dummy != None):
            m += 1
            dummy = dummy.next
        
        if m == n:
            return head.next
        
        
        
        for _ in range(m-n-1):
            #dummyTwo at prev Position
            dummyTwo = dummyTwo.next
        
        dummyTwo.next = dummyTwo.next.next
        
        
        return head
        