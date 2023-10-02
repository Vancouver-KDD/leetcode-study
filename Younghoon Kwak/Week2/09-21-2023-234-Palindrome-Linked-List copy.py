# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head.next is not None:
            l.append(head.val)
            head = head.next
        l.append(head.val)
        left = 0
        right = len(l) - 1
        n = len(l)
        ans = True
        for i in range(n/2):
            if l[left] != l[right]:
                ans = False
            else: 
                left += 1
                right -= 1
        
        return ans
            