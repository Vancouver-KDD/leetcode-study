# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check one of input is None
        if not list1:
            return list2
        if not list2:
            return list1
        
        # set initial node
        if list1.val <= list2.val:
            init = list1
            head = list1
            list1 = list1.next
        else:
            init = list2
            head = list2
            list2 = list2.next
        
        while list1 and list2:
            # merge with list1 node
            if list1.val <= list2.val:
                init.next = list1
                list1 = list1.next
            # merge with list2 node
            else:
                init.next = list2
                list2 = list2.next
            init = init.next
        
        # add leftover nodes
        if not list1:
            init.next = list2
        if not list2:
            init.next = list1
        
        return head

