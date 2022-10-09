class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2, tmp = cost[-2], cost[-1], 0

        for idx in range(len(cost)-3, -1, -1):
            tmp = dp1
            dp1 = min(dp1 + cost[idx], dp2 + cost[idx])
            dp2 = tmp
        
        return min(dp1, dp2)

