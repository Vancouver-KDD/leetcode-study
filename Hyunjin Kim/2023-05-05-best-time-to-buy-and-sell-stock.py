class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = 10 ** 5

        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(max_profit, p - min_price)
        return (max_profit)
