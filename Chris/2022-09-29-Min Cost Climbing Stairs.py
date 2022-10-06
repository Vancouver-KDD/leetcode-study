class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        l = len(cost)
        dp = [0] * (l + 2)
        
        
        for i in range(2,l+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        dp[l+1] = dp[l-1] + cost[l-1]
        return min(dp[l], dp[l+1])