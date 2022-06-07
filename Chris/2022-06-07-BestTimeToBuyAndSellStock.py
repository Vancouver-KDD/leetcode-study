class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0
        
        for price in prices:
            if(price-lowest > maxProfit ):
                maxProfit = price-lowest
            
            if(lowest > price):
                lowest = price
        
        
        return maxProfit