class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = head

        while visited:
            if visited.val == None:
                return True

            visited.val = None  ## makring visitied
            visited = visited.next  ## move on to the next

        return False

        ## TC: O(n)