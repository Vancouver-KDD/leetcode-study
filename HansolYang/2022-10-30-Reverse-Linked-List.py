# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = deque()
        while head:
            arr.appendleft(head.val)
            head = head.next
        if not arr or len(arr) == 0:
            return None
        
        ret = ListNode(arr[0])
        p = ret
        arr.popleft()
        
        for i in arr:
            p.next = ListNode(i)
            p = p.next
        
        return ret