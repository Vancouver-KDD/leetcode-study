#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        dummy=ListNode(0)
        dummy.next=head

        prev=dummy
        cur=dummy.next

        for i in range(1,left):
            cur=cur.next
            prev=prev.next

        for i in range(right-left): # Right: 5, Left: 3 (Right - Left = 2)
            temp=cur.next # 1, 2(Prev), 3(Cur), 4(Temp), 5(Temp.Next), 6 
            cur.next=temp.next # Move Cur to Next Node 
            temp.next=prev.next # Move Prev Next to 
            prev.next=temp  # Move what that next to cur to the pre next 

        # Startegy
        # Move Cur to the back for every move 
        # Move what's next to current node to the beginning of the reversed list
        # Move back what's here




        return dummy.next

