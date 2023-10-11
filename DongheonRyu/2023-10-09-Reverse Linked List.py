def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev


# 1 -> 2 -> 3 -> 4
#           

def reverseListRecursion(head):
      if not head:
            return None
      
      newHead = head # 4
      if head.next: # 4
            newHead = reverseListRecursion(head.next) #4
            head.next.next = head
      head.next = None

      return newHead