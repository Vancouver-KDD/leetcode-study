class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1} # base condition
        
        for sub in range(1,target +1):
            dp[sub] = 0 #initialize
            for eachNum in nums:
                dp[sub] += dp.get(sub-eachNum, 0)
        return dp[target]