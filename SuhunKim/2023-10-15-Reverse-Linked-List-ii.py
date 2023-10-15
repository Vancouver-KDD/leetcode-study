# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li = []
        left, right = left-1, right-1
        
        while head:
            li.append(head.val)
            head = head.next
        
        to_reverse = list(reversed(li[left:right+1]))
        
        new_list = li[:left] + to_reverse + li[right+1:]
        
        new_node = ListNode()
        new_head = new_node
        
        while new_list:
            val = new_list.pop(0)
            new_node.next = ListNode(val)
            new_node = new_node.next
            
        return new_head.next