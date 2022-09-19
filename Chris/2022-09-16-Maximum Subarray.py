class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = localMax = nums[0]
        
        for num in nums[1:]:
            
            if localMax >= 0:
                localMax += num
            else:
                localMax = num
            
            if localMax > res:
                res = localMax
        
        
        return res
        