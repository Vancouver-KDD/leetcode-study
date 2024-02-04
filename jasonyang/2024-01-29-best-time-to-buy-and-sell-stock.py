# 121. Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# 
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize the minimum price to infinity
        max_profit = 0  # Initialize the maximum profit to 0

        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)

            # Calculate the profit for the current price and update the maximum profit if it's higher
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

# Example usage
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(sol.maxProfit([7, 6, 4, 3, 1]))  # Output: 0