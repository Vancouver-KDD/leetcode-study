# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        lastNode = head
        count = 1
        # You should use "is not" or "is" when you compare to None
        # None is a singleton in Python, there is only one instance of it in memory
        # By comparing identity, this can be performed very quickly. 
        # Python checks whether the object you're referring to has the same memory address 
        # as the global None object - a very, very fast comparison of two numbers.
        while lastNode.next is not None:
            temp = lastNode
            lastNode = lastNode.next
            lastNode.prev = temp
            count += 1
        lastNode.next = head
        head.prev = lastNode
        
        if k > count:
            k = k % count
            
        currentNode = head
        for i in range(0, k + 1):
            currentNode = currentNode.prev
        head = currentNode.next
        currentNode.next = None
        
        return head        
            
        
            
        