# KDD LeetCode Study Week 8: Heap / Priority Queue
# Assignment 2
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/merge-k-sorted-lists

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = ListNode(0)
        curr = tmp
        data = []

        for node in lists:
            while node:
                heapq.heappush(data, node.val)
                node = node.next
        
        while data:
            val = heapq.heappop(data)
            curr.next = ListNode(val)
            curr = curr.next

        return tmp.next