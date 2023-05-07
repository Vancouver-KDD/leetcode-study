# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # result = 0
        # case no profit : prices len == 0
        length_price = len(prices)
        if length_price == 1 or prices == sorted(prices, reverse=True):
            return 0

        max_profit = 0
        min_price = 2**63-1

        for i in range(length_price):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(prices[i] - min_price, max_profit)

        return max_profit

