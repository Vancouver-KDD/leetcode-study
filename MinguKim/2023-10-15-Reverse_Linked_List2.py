# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #using dummy ListNode(0) from https://www.youtube.com/watch?v=oDL8vuu2Q0E
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        index=0
        for i in range(left-1):
            prev = prev.next
        curr = curr.next
        for i in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            index+=1
        if left == right:
            return head
        if prev.val==0:
            return prev.next
        return prev