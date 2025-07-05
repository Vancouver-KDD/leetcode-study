# KDD LeetCode Study Week 5: Linked List
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/linked-list-cycle-ii

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current
            
            visited.add(current)
            current = current.next
        
        return None