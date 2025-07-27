import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        res = 0

        for i in range(len(nums)):
            heapq.heappush(max_heap, -nums[i])

        for _ in range(k):
            res = -heapq.heappop(max_heap)

        return res