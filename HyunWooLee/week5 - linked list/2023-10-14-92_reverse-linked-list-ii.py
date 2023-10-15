class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''

         p

    d -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
         t

                        p    reverse_node
         <---2 <--3 <---4    next


    d ->1 -> 4 -> 3->2 ->None  5 -> 6

    '''

    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head

        tmp = dummy

        for i in range(m - 1):
            tmp = tmp.next

        prev = None
        reverse_node = tmp.next
        for i in range(n - m + 1):
            next_item = reverse_node.next
            reverse_node.next = prev
            prev = reverse_node
            reverse_node = next_item

        # order matters
        tmp.next.next = reverse_node
        tmp.next = prev

        return dummy.next