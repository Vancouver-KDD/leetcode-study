# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        l1_str, l2_str = "", ""
        while cur:
            l1_str = str(cur.val) + l1_str
            cur = cur.next

        cur = l2
        while cur:
            l2_str = str(cur.val) + l2_str
            cur = cur.next
        res_str = str(int(l1_str) + int(l2_str))
        dummy_head = ListNode()
        dummy_head.next = ListNode()
        cur = dummy_head.next
        for i in range(len(res_str)-1,-1,-1):
            cur.val = int(res_str[i])
            if not i == 0:
                cur.next = ListNode()
                cur = cur.next
        return dummy_head.next
