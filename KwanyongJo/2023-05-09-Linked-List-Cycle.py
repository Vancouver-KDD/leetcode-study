# Given head, the head of a linked list,
# determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                # print(head.val)
                return True
            seen.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)


    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2

    s = Solution()
    print(s.hasCycle(l1))