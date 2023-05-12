# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head.next:
            if head.next.val in list:
                return True
            else:
                list.append(head.next.val)
                head = head.next
        return False