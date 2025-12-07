class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0

        dp = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin <= amount: 
                dp[coin] = 1

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                
        return -1 if dp[amount] == float('inf') else dp[amount]        