from collections import deque
import heapq
from typing import Counter

class Solution:
    def leastInterval(self, tasks, n):
        
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()
        
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time


solution = Solution()
print(solution.leastInterval(["A", "C", "A", "B", "D", "B"], 1))
