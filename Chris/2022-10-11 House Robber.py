class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        
        #dp[i] = max profit when robbing until i_th house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]
        
        