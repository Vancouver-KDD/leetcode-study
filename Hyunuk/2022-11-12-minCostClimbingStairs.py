class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        priceHistory = [cost[0], cost[1]]
        for i in range(2, len(cost)+1):
            curr = cost[i] if i < len(cost) else 0
            temp = min(priceHistory[i-2] + curr, priceHistory[i-1] + curr)
            priceHistory.append(temp)
        return priceHistory[-1]
