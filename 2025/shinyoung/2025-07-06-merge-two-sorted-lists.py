# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 and list2:
            if list1.val < list2.val:
                curr = ListNode(list1.val, None)
                list1 = list1.next
            else:
                curr = ListNode(list2.val, None)
                list2 = list2.next
        elif list1:
            curr = ListNode(list1.val, None)
            list1 = list1.next
        elif list2:
            curr = ListNode(list2.val, None)
            list2 = list2.next
        else:
            return None

        head = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, None)
                list2 = list2.next
            curr = curr.next

        while list1:
            curr.next = ListNode(list1.val, None)
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = ListNode(list2.val, None)
            list2 = list2.next
            curr = curr.next

        return head

solution = Solution()
print(solution.mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None)))))

