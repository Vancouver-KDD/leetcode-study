# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        removes nth node from the end of the list.
        returns head.

        1. If n = 1, remove tail node
        2. If n = length of linked list, remove head and second node will be head
        3. if n > list, return false or None 
        4. if n = 2 ~ (length of linked list) -1, next property of n-1 node assgines n+1 node


        """
#         next = head
#         prev = None
#         count = 1
#         while next.next:
#             prev = next
#             next = next.next
#             count += 1

#         if n == count:
#             head = head.next
#             return head

#         elif n > count:
#             return head

#         elif n == 1:
#             prev.next = None
#             return head
#         else:
#             index = count - n
#             node = head
#             prev = None
#             for index in range(index):
#                 prev = node
#                 node = node.next
#             prev.next = node.next                
#             return head

        dummy = ListNode(0, head) 
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next