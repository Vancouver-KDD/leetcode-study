class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        prehead = ListNode(-1)
        prev = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1 is not None:
            prev.next = list1
        else:
            prev.next = list2

        return prehead.next 
