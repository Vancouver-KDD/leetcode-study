# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            first = list1
            second = list2
        else:
            head = list2
            first = list2
            second = list1
        while first.next and second:
            if first.next.val > second.val:
                first_temp = first.next
                second_temp = second.next
                first.next = second
                second.next = first_temp
                first = second
                second = second_temp
            else:
                first = first.next
        if second:
            first.next = second
        return head