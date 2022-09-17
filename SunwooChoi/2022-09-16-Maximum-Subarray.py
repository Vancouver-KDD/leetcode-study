class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_max, cur_sum = nums[0], nums[0]
        
        for idx in range(1, len(nums)):
            cur_sum += nums[idx]

            # if the current sum is less than the current element,
            # set the current sum to the current element
            if cur_sum < nums[idx]:
                cur_sum = nums[idx]
            
            # revalue the current max 
            cur_max = max(cur_sum, cur_max)
        
        return cur_max