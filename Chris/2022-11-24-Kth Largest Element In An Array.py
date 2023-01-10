class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        pop_times = len(nums) - k
        for _ in range(pop_times):
            heapq.heappop(nums)
        
        return nums[0]