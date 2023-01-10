# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_middle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(node):
            prev, curr, next_ = None, node, node.next
            while curr:
                curr.next = prev
                prev = curr
                curr = next_
                next_ = next_.next if next_ else None
            return prev
        
        dummy = ListNode(-1)
        dummy.next = head
        middle = find_middle(head)
        tail = reverse(middle)
        is_head_turn = True
        
        while tail.next:
            if is_head_turn:
                temp = head.next
                head.next = tail
                head = temp
            else:
                temp = tail.next
                tail.next = head
                tail = temp
            is_head_turn = not is_head_turn
        return dummy.next
