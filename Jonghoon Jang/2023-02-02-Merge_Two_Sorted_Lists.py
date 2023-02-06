"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n + m): travers both lists
    # Space complexity: O(n + m): n + m stacks
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dum = ListNode()
        ans_head = dum
        while list1 and list2:
            if list1.val <= list2.val:
                dum.next = ListNode(list1.val)
                dum = dum.next
                list1 = list1.next
            else:
                dum.next = ListNode(list2.val)
                dum = dum.next
                list2 = list2.next

        if list1:
            dum.next = list1
        if list2:
            dum.next = list2


    # Time complexity: O(n + m): travers both lists
    # Space complexity: O(1):
    def mergeTwoListsRecur(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def create_linked_list(self, items):
        curr = None
        head = None
        for item in items:
            new_node = ListNode(item)
            if not head: # curr is None
                head = new_node
                curr = new_node
            else:
                curr.next = new_node
                curr = curr.next
        return head


    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()


def main():
    s = Solution()


if __name__ == "__main__":
    main()
