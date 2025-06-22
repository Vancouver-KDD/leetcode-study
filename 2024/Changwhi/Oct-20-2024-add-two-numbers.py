# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. make it string
        2. concatenate them, add new char to the first place
        3. convert string to integer, and add them
        4. store in a linked list and return the head?
        
        Or
        
        you can do during looping through the given linked lists.
        
        1. Loop thorugh the linked lists
        2. add each numbers and store the result in a new node.
        3. if the result exceeds 9, then increment next result by 1.
        """

        newHead = ListNode(0, None)
        dummy = newHead
        remain = 0

        while l1 or l2 or remain:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            result = first + second + remain
            
            remain = result // 10
            result = result % 10

            
            newHead.next = ListNode(result, None)
            newHead = newHead.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
        