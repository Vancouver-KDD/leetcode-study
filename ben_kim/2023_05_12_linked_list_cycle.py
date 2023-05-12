class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next: # 1
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False

# 1. Since fast reaches the end of the list first, we need to check for fast instead of slow in the conditional statement