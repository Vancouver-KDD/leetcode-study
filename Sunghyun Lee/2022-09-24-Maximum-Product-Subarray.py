class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        prevMax = nums[0]
        prevMin = nums[0]
        result = currentMax
        for i in range(1,len(nums)):
            val = nums[i] 
            currentMax = max(prevMax * val, prevMin * val, val)
            currentMin = min(prevMax * val, prevMin * val, val)
            
            prevMax = currentMax
            prevMin = currentMin
            
            result = max(currentMax, result)
        return result
