# 21. Merge Two Sorted Lists

> Problem link: https://leetcode.com/problems/merge-two-sorted-lists/  
> submission detail: https://leetcode.com/submissions/detail/833718573/  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # 둘중 하나가 마지막까지 도달했다면 tail은 남아있는 리스트를 바라보게하면 된다        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
        
```