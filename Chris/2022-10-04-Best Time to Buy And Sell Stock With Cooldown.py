class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        # key : (index, canBuy) 
        # value : maxProfit
        dp = {}
        
        
        # Return max profit starting from index i from prices and canBuy statea
        def dfs(i, canBuy):
            
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            
            # Cooldown at prices[i] which can be done in any state
            cooldown = dfs(i+1, canBuy)
            
            
            if canBuy:
                # Buying prices[i]
                buy = dfs(i+1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(cooldown, buy)
            else:
                # Selling at prices[i]
                sell = dfs(i+2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(cooldown, sell)
            
            return dp[(i, canBuy)]
        
        dfs(0, True)
        
        return dp[(0, True)]
                