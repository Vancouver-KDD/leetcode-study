# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if not head:
                return None 
            
            tail = head
            nodeLen = 1
            while tail.next:
                tail = tail.next 
                nodeLen += 1
            tail.next = head # cycle 51234512345...
            rotateType = k % nodeLen # 2
            
            temp = head # 1234512345...
            for _ in range(nodeLen - rotateType - 1): # 5-2-1 = 2
                temp = temp.next # 3
            res = temp.next # 4512345...
            temp.next = None # 45123

            return res