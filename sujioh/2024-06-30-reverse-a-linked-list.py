class Solution(object):
    def reverseList(self, head): 
        curr = head
        prev = None

        while curr:
            next_curr = curr.next 
            
            # main execution 
            curr.next = prev

            # prepare for next execution 
            prev = curr  
            curr = next_curr # 2 # 3
        
        return prev