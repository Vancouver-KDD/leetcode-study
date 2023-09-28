# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ### method 1 (iterate twice, store all linked list in the list) Time: O(n), Space: O(n)
        # li = []
        # curr = head
        # while curr:
        #     li.append(curr)
        #     curr = curr.next
        # to_be_removed = li[-n]
        # curr = head
        # while curr:
        #     if curr.next == to_be_removed:
        #         curr.next = to_be_removed.next
        #     if curr == to_be_removed and curr == head:
        #         head = curr.next
        #     curr = curr.next
        # return head
        
#         ### method 2 (recursion) Time: O(n), Space: O(n)
#         def helper(head, curr):
#             if not curr:
#                 return 1
#             nth_from_tail = helper(head, curr.next)
#             if nth_from_tail == n and curr == head:
#                 return -1
#             elif nth_from_tail == n+1:
#                 curr.next = curr.next.next
#             return nth_from_tail+1
            
#         curr = head
#         if helper(head, curr) == -1:
#             return head.next
#         else:
#             return head
        
#         ### method 3 (iteration without storing into a list); Time: O(n), Space: O(1)
#         curr = head
#         max_depth = -1
#         while curr:
#             max_depth += 1
#             curr = curr.next

#         curr = head
#         depth = 0
#         while curr:
#             if max_depth - depth == n-1 and curr == head:
#                 head = curr.next
#             elif max_depth - depth == n:
#                 curr.next = curr.next.next
#             curr = curr.next
#             depth += 1
            
#         return head

        ### method 4 (two pointers) ###
        if not head:
            return None
        slow, fast = ListNode(0, head), ListNode(0, head)
        
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        if slow.next == head:
            return head.next
        else:
            slow.next = slow.next.next
            return head