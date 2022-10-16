class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         if len(nums) <= 3:
#             return max(nums)
        
#         dp1 = [0] * len(nums)
#         dp2 = [0] * len(nums)
        
#         #first, ignore the nums[0]
#         dp1[1] = nums[1]
#         for i in range(2, len(nums)):
#             dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        
#         #second, ignore the nums[-1]
#         dp2[1] = nums[0]
#         for i in range(2, len(nums)):
#             dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i-1])
            
        
#         return max(dp1[-1], dp2[-1])
    
        if len(nums) <= 3:
            return max(nums)
        
        #first, ignore the nums[0]
        dp1 = nums[1]
        dp2 = max(nums[1], nums[2])
        
        for i in range(2, len(nums) - 1):
            temp = dp1
            dp1 = dp2
            dp2 = max(dp1, temp + nums[i + 1])
        
        curr_max = dp2
        
        #second, ignore the nums[-1]
        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        
        for i in range(2, len(nums) - 1):
            temp = dp1
            dp1 = dp2
            dp2 = max(dp1, temp + nums[i])
        
        return max(curr_max, dp2)
    