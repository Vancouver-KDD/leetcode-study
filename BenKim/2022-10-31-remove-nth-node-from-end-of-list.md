# 19. Remove Nth Node From End of List

> Problem link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
> submission detail: https://leetcode.com/submissions/detail/833854516/

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 가상의 0번째 노드         
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # n번째의 노드를 제거하기위해서 left가 n-1번째에 위치해야 한다        
        # right는 head에서부터 n만큼 이동        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        
        return dummy.next
        

```
