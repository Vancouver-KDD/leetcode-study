# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5]
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None

        while curr:  # 1 #2 #3
            temp = curr.next  # 2 #3 #None
            curr.next = prev  # 1.next = none #1 #2
            prev = curr  # prev = 1 #2 #3
            curr = temp  # curr = 2 #3 None

        return prev


# 12345
# 5.next = 4
# 2.next = 1
