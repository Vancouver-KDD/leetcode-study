# 206. Reverse Linked List

> Problem link: https://leetcode.com/problems/reverse-linked-list/  
> submission detail: https://leetcode.com/submissions/detail/833379444/  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            # 다음노드 임시저장             
            tmp = curr.next
            
            # 포인터 방향변경             
            curr.next = prev
            
            # 다음스텝으로 이동             
            prev = curr
            curr = tmp
        return prev
```