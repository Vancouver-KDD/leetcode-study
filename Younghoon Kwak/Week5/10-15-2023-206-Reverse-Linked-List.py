class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Create a new list
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list # null <- 1 <- 2
            new_list = current # new_list : null <- 1 
            current = next_node # current -> 2
        
        return new_list
    
        # 1-> 2 -> 3 -> 4 -> 5
        # null <- 1 <- 2 <-3 

