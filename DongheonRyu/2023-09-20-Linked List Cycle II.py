
# hash set => o(n), o(n) 
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hash_set = set()

        while head:

            if head in hash_set:
                return head
            hash_set.add(head)
            head = head.next

        return None    