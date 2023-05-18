# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# https://peterdrinker.tistory.com/491

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, value: int) -> int:
        heapq.heappush(self.min_heap, value)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        print(self.min_heap)
        return self.min_heap[0]
    
list = [4, 5, 8, 2]
kth = KthLargest(3, list)
print(kth.add(3))
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))