# 141. Linked List Cycle

> Problem link: https://leetcode.com/problems/linked-list-cycle/  
> submission detail: https://leetcode.com/submissions/detail/833691237/

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        
        # cycle이 없는경우 fast노드가 먼저 마지막에 도착한다         
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 2칸, 1칸이동이기때문에 매번 -1만큼 거리가 좁혀진다
            if slow == fast:
                return True
        
        return False
```
