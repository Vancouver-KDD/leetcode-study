class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reversed_k = len(nums) - k + 1
        heapq.heapify(nums)
        curr = 0
        count = 1
        while 1:
            curr = heapq.heappop(nums)
            if count == reversed_k:
                return curr
            count += 1
