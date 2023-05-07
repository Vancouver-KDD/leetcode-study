class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        profit = sell - buy
        for i in range (len(prices)):            
            if buy > prices[i]:
                buy = prices[i]                
            if buy < prices[i]:                
                if profit < prices[i] - buy:
                    sell = prices[i]
                    profit = sell - buy                    
        return profit