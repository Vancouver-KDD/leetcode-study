class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        
        return new_list


# Solution 2: Recursive Method 
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return None

#         new_head = head
#         if head.next:
#             new_head = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return new_head
#Time complexity: O(n)
#Space complexity: O(n). 