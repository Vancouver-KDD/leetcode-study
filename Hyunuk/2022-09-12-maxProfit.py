class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        ret = 0
        for i in range(len(prices)):
            curr = prices[i]
            buy = min(buy, curr)
            if buy < curr:
                ret = max(ret, curr - buy)
        return ret
