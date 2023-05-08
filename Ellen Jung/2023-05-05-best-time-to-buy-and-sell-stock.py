class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        min_profit = 0
        for i in range (0, length-1):
            for j in range (i+1, length):
                profit = prices[j] - prices[i]
                if profit > 0 and profit > min_profit:
                    min_profit = profit

        return min_profit