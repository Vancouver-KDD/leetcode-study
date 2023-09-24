class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### method 1 (using set) => Time: O(n), Space: O(n) ###
        s = set()
        curr = head
        while curr:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None