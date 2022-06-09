from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num, max_profit = prices[0], 0
        for idx, num in enumerate(prices):
            min_num = min(min_num, num)
            max_profit = max(num-min_num, max_profit)
        return max_profit
