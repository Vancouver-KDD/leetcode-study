# 143. Reorder List

> Problem link: https://leetcode.com/problems/reorder-list/  
> submission detail: https://leetcode.com/submissions/detail/834701694/  

- 투포인터를 이용해 Linked List의 중간점을 찾기
```py
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
        slow, fast = head, head.next
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```