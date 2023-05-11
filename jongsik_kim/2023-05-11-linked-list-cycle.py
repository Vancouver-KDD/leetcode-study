from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialize the hashmap and index
        # hashmap: {head(value), index}
        hashmap, index = {}, 0
        if not head or not head.next:
            return False
        while head.next:
            if head.next in hashmap:
                return True
            hashmap[head] = index
            index += index
            head = head.next
        return False
