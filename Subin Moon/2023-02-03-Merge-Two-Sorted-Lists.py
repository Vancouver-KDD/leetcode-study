"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: Brute Force
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = ListNode()
        res_head = res

        while list1 and list2:
            if list1.val < list2.val:
                res_head.next = list1
                list1 = list1.next
            else:
                res_head.next = list2
                list2 = list2.next

            res_head = res_head.next

        if list1:
            res_head.next = list1
        elif list2:
            res_head.next = list2

        return res

    # Solution 2: Recursive
    def mergeTwoLists_recursive(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)

        return list1