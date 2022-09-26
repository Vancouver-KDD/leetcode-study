class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        maxprofit = 0
        
        for i in prices[1:]:
            if i < buy:
                buy = i
            
            if (i - buy) > maxprofit:
                maxprofit = (i - buy)
        
        return maxprofit