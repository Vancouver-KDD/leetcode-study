class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        sold, held, none = float("-inf"), float("-inf"), 0

        for p in prices:
            t_sold = sold
            sold = held + p
            held = max(held, none - p)
            none = max(none, t_sold)
        return max(sold, none)