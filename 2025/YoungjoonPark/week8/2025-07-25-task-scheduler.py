# KDD LeetCode Study Week 8: Heap / Priority Queue
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/task-scheduler

from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        cooldown_queue = deque()
        
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                count = cooldown_queue.popleft()[0]
                heapq.heappush(max_heap, count)
            
            if max_heap:
                current_count = heapq.heappop(max_heap)
                
                current_count += 1
                
                if current_count < 0:
                    cooldown_queue.append((current_count, time + n + 1))
                    
        return time