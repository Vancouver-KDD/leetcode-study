# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
import sys


class Solution:
    # Solution 1: Brute force - Using two pointers O(n^2)
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        # Iterate the prices array
        # Get all possible profit for each element and replace the max_profit everytime it gets bigger profit
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j] - prices[i]
                if max_profit < curr_profit:
                    max_profit = curr_profit

        if max_profit < 0:
            return 0
        else:
            return max_profit

    # Solution 2
    def maxProfit_2(self, prices: list[int]) -> int:
        min_price = sys.maxsize
        profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
