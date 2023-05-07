class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur_min = prices[0]
        profit = 0

        for price in prices:
            if price < cur_min:
                cur_min = price
            else:
                profit = max(profit, price - cur_min)

        return profit