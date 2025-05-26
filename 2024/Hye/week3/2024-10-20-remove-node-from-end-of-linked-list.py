"""
Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

python3 Hye/week3/2024-10-w3-remove-node-from-end-of-linked-list.py

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        k = length - n + 1
        if k < 0:
            return head
        elif k == 1:
            return head.next
        
        curr = head
        prev = None
        count = 1
        while curr:
            if count == k and prev is not None:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            count += 1
        
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
    head = [1,2,3,4]
    list_node = build_node(head)
    n = 2
    expected_output = [1,2,4]
    output = sol.removeNthFromEnd(list_node, n)
    for i in range(len(expected_output)):
        assert output.val == expected_output[i]
        output = output.next
    print("True")

    print("Example 2")
    head = [5]
    list_node = build_node(head)
    n = 1
    expected_output = []
    output = sol.removeNthFromEnd(list_node, n)
    for i in range(len(expected_output)):
        assert output.val == expected_output[i]
        output = output.next
    print("True")

    print("Example 3")
    head = [1,2]
    list_node = build_node(head)
    n = 2
    expected_output = [2]
    output = sol.removeNthFromEnd(list_node, n)
    for i in range(len(expected_output)):
        assert output.val == expected_output[i]
        output = output.next
    print("True")


if __name__ == "__main__":
    main()
