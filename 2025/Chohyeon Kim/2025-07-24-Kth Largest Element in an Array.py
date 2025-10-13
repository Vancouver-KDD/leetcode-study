class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [-n for n in nums]

        heapq.heapify(max_heap)

        print(max_heap)

        i = 0
        res = None

        while i != k:

            res = heapq.heappop(max_heap)

            i += 1

        return -res
