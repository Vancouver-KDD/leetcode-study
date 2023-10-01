# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = True
        first_end = self.end_of_first_half(head)
        second_start = self.reverse_list(first_end.next)

        first = head
        second = second_start
        while first and second:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next
        
        return result