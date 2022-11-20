class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         if len(nums) <= 2:
#             return max(nums[0], nums[-1])
        
#         dp = [0] * (len(nums))
#         dp[0] = nums[0]
#         dp[1] = nums[1]
        
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#             print(dp[i-1], dp[i-2] + nums[i])
        
#         return dp[-1]

        if len(nums) <= 2:
            return max(nums[0], nums[-1])
        
        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        index = 2
        
        while index < len(nums):
            temp = dp1
            dp1 = dp2
            dp2 = max(temp + nums[index], dp2)
            index += 1
            
        
        return max(dp1, dp2)