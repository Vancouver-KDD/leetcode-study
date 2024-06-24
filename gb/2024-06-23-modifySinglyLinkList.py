# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Solution:
    def reorderList(self, head):

        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        # while f.next and f.next.next:
        #     s = s.next
        #     f = f.next.next

        # reverse s is the head of the second half
        secondDummy = s
        head2 = secondDummy.next
        s.next = None

        # reverse
        prevNode = None
        currNode = head2
        while currNode:
            tmp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tmp

        def merge(first, second):
            while first and second:
                tmp1, tmp2 = first.next, second.next
                first.next = second
                second.next = tmp1
                first = tmp1
                second = tmp2
        merge(head, prevNode)

        return head
