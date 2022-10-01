class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        res, localMax, localMin = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            prevLocalMax = localMax 
            localMax = max(num, localMin*num, prevLocalMax*num)
            localMin = min(num, localMin*num, prevLocalMax*num)
            res = max(res, localMax)
            
        return res    
                