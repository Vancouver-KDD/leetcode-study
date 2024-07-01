# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Go over the linked list and push nodes to stack while finding kth node from the start
        # 2. Pop nodes from stack to find kth node from the end
        # 3. Swap two nodes

        k_from_start = None
        k_from_end = None
        curr = head
        index = 1
        stack = []
        while curr:
            if index == k:
                k_from_start = curr
            stack.append(curr)
            curr = curr.next
            index += 1

        index = 1
        while len(stack):
            this_node = stack.pop()
            if index == k:
                k_from_end = this_node
                break
            index += 1
        k_from_start.val, k_from_end.val = k_from_end.val, k_from_start.val

        return head
