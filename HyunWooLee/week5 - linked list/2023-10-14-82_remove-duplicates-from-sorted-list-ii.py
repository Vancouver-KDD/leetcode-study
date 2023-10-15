# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''

              p
    d -> 1 -> 2 -> 3 -> 3 -> 4 -> 5
                             c


    - Whenever you have a potential to have first element of LL being excluded, always use dummy node in front of head
    - It's always easier to look ahead and advance pointers rather than the advance pointer, then fix
        (personal opinion; this is evident in singly Linked List because we always go from curr node to next
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = curr
                curr = curr.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next
                curr = curr.next

        return dummy.next