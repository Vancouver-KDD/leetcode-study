def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val ==val:
            head = head.next
        
        if not head:
            return head
        
        current = head
        while current:
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head