
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i) # 1
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap, i) # 2

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
# 1. heap queue, priority queue
# 2. Create a heap with k elements, and if it is greater than the minimum value (heap[0]), replace elements using pushpop.