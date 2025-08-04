class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node
        return new_head
