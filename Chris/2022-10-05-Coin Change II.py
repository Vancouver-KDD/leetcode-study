class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        # dp[i] : combinations summing up to amount i
        dp = [0] * (amount+1)
        
        dp[0] = 1
        
        
        for c in coins:
            for i in range(1,amount+1):
                if i - c >= 0:
                    dp[i] += dp[i-c]
        return dp[-1]
            
        
        