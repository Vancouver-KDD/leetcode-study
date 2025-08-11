class Solution:
    def coinChange(self, coins, amount):
        # Bottom Up DP(Tabulation)
        # Time: (number of coins * amount)
        # Space: O(amount)
        
        dp=[0]*(amount+1)
        
        for i in range(1, amount+1):
            minn=float('inf')
            
            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                minn=min(minn, dp[diff]+1)
            
            dp[i]=minn
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
    

solution = Solution()
print(solution.coinChange([1, 2, 5], amount=11))
print(solution.coinChange([2], amount=3))
print(solution.coinChange([1], amount=0))
