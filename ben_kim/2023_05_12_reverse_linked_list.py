     
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, curr = None, head

        while curr:
            next = curr.next # 1
            
            curr.next = prev

            prev = curr
            curr = next

        return prev # 2

# 1. Before changing direction, save the next node temporarily
# 2. Since the while loop executes until the last node, the head ends up moving to null


