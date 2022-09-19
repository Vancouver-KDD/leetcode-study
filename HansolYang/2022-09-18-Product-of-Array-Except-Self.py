class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1 for i in range(len(nums))]
        
        start = 1
        for i in range(len(nums)):
            res[i] *= start
            start *= nums[i]
        
        end = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= end
            end *= nums[i]
        
        return res