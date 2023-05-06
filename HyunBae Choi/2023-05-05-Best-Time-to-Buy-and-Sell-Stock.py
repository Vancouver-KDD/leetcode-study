# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can approach this problem as a "sliding window" problem using two pointers
        # first start by moving the right pointer and calculate the profit between the two pointers
        # compare and store the bigger value between the current profit and the max profit
        # then, keep moving the right pointer until it gets to the end
        # if at any point the left pointer value is more than the right pointer value, that means we found our new lowest point
        # therefore, move the left pointer to the new right pointer position

        left_pointer = 0
        right_pointer = 1
        max_profit = 0

        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, profit)
            else:
                left_pointer = right_pointer
            right_pointer += 1

        return max_profit
