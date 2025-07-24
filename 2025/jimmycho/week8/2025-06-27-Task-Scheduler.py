from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)
        queue = deque([])
        res = 0
        while max_heap or queue:
            if queue and queue[0][1] < res:
                heapq.heappush(max_heap, -queue.popleft()[0])
            if not max_heap:
                res += 1
                continue
            priority_task = -heapq.heappop(max_heap)
            if priority_task - 1 > 0:
                queue.append([priority_task - 1, res + n])
            res += 1
        return res
