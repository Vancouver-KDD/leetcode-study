from typing import Optional
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # find the node which is not pointing the next node of it.
        # compare with the length. --> time limit exceeded, not able to get the length if it is cycled.
        # save each address of the node into set.
        visit = set()

        while head:
            if id(head) in visit:
                return True

            visit.add(id(head))
            head = head.next

        return False

