class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0
        
        
        for p in prices:
            
            if p < lowest:
                lowest = p
            else:
                maxProfit = max(maxProfit, p - lowest)
        
        return maxProfit