# Definition for singly-linked list.
from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        #will save the reverse node in ans
        ans = None

        while node :
            #save next nodes for next loop
            next_list = node.next
            #replace next nodes to answerlist to connect current node to answerlist
            node.next = ans
            #save the changed node to ans
            ans = node
            #change the node to saved node.next for next loop
            node = next_list

        return (ans)
