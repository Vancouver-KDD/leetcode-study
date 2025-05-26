""" Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list 
and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100

python3 Hye/week3/2024-10-w3-merge-two-sorted-linked-list.py

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Start with the node with smaller value while both lists are not None
        2. the curr.next will be the next larger value when comparing list1 and list2
        3. If either one of the lists reaches the end, curr follows the rest of the remaining list
        """
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = curr = list1
            list1 = list1.next
        else:
            head = curr = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        
        if list1 is not None:
            curr.next = list1
        if list2 is not None:
            curr.next = list2
        
        return head


def build_node(list):
    head = None
    for i in range(len(list)):
        node = ListNode(list[i])
        if i == 0:
            head = curr = node
        else:
            curr.next = node
            curr = curr.next
    return head


def main():
    sol = Solution()
    print("Week 3: Merge Two Sorted Linked Lists")
    
    print("Example 1")
    list1 = build_node([1,2,4])
    list2 = build_node([1,3,5])
    expected_output = [1,1,2,3,4,5]
    head = sol.mergeTwoLists(list1, list2)
    for i in range(len(expected_output)):
        assert head.val == expected_output[i]
        head = head.next
    print("True")
    
    print("Example 2")
    list1 = build_node([])
    list2 = build_node([1,2])
    expected_output = [1,2]
    head = sol.mergeTwoLists(list1, list2)
    for i in range(len(expected_output)):
        assert head.val == expected_output[i]
        head = head.next
    print("True")

    print("Example 3")
    list1 = build_node([])
    list2 = build_node([])
    expected_output = []
    head = sol.mergeTwoLists(list1, list2)
    assert head == None
    print("True")


if __name__ == "__main__":
    main()
