class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        left, right = head, head.next
        while right and right.next:
            left = left.next
            right = right.next.next
        second = left.next
        left.next = None
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
        
        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            head.next.next = tmp1
            head = tmp1
            prev = tmp2