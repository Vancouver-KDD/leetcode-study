class Solution:
    def maxProfit(self,prices):
        l, r = 0, 1
        res = 0
    
        while r < len(prices):
            lp = prices[l]
            rp = prices[r]
            
            if lp < rp:
                res = max(res, rp - lp)
            else: 
                l = r
            r += 1
        
        return res