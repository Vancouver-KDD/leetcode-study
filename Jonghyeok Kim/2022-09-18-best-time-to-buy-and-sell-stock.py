class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init 2 pointers
        res, min_price = 0, prices[0]
        # update min price and max return by iterating the list
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > res:
                res = price - min_price
        return res