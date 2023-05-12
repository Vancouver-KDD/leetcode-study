class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # 1
        cur = dummy
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1 # 2
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# 1. The dummy pointer is fixed at the initial value, and the curr pointer moves.

# 2. Order is important.
# cur = list1 [O]
# list1 = list1.next 
# 
# list1 = list1.next [X]
# cur = list1