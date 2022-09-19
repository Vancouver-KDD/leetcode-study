class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_lowest = prices[0]
        
        for idx in range(len(prices)):
            cur_price = prices[idx]
            
            # track lowest price in the past
            if cur_lowest > cur_price:
                cur_lowest = cur_price
                continue
            
            cur_profit = cur_price - cur_lowest
            profit = max(profit, cur_profit)
        
        return profit
