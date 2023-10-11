def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

def reverseListRecursion(head):
      if not head:
            return None
      
      newHead = head
      if head.next:
            newHead = reverseListRecursion(head.next)
            head.next.next = head
      head.next = None

      return newHead