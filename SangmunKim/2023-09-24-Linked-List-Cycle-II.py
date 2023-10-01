class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        turtle = head

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next

            if turtle == rabbit:
                break
        
        if not rabbit or not rabbit.next:
            return None
        
        rabbit = head

        while turtle != rabbit:
            turtle = turtle.next
            rabbit = rabbit.next
        
        return turtle
