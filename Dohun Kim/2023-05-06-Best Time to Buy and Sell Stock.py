class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minimum = 10**4
        for p in prices:
            minimum = min(minimum, p)
            profit = p-minimum
            maxProfit = max(maxProfit, profit)
        return maxProfit