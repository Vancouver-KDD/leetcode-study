# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         lastNode = head

#         while lastNode.next: 
#             temp = lastNode
#             lastNode = lastNode.next
#             lastNode.prev = temp
        
#         leftNode = head
#         rightNode = lastNode
#         for i in range(0, k - 1):
#             leftNode = leftNode.next
#             rightNode = rightNode.prev
        
#         temp = leftNode.val
#         leftNode.val = rightNode.val
#         rightNode.val = temp
        
#         return head

#         lastNode = head
#         count = 1
#         while lastNode.next:
#             count += 1
#             lastNode = lastNode.next
        
#         KfromRight = count - k
#         KfromLeft = k 
        
#         rightNode = head
#         leftNode = head
#         for i in range(0, KfromRight):
#             rightNode = rightNode.next
        
#         for i in range(0, KfromLeft - 1):
#             leftNode = leftNode.next
            
#         temp = leftNode.val
#         leftNode.val = rightNode.val
#         rightNode.val = temp
        
#         return head
        
        left=right=head
        for i in range(1,k):
            left=left.next

        temp=left
        while temp.next:
            right = right.next
            temp=temp.next
        left.val,right.val=right.val,left.val
        return head