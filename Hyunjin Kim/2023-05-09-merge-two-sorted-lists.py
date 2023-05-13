# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head refer to the first node of the answer list
        head = ListNode()
        # curr will be used for pointing next node.
        curr = head

        # escape loop while list1 or lis2 is not None
        while list1 and list2:
            if list1.val >= list2.val:
                # connect list2 to the answer listnode
                curr.next = list2
                # move to the next node in list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            # move to next node in answerlist for next loop
            curr = curr.next

        # connect remaining nodes to the answerlist
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2
        return (head.next)
