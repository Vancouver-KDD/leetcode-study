class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums) + 2)]
        
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        
        
        return dp[0]