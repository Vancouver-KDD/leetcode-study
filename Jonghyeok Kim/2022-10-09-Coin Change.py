class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for idx in range(amount+1):
            #Try each coin and find out the smallest combination
            for coin in coins:
                #If coin is bigger than the index, coin can not fit. 
                #If it is smaller or equal, update the element with smaller combination
                if coin <= idx:
                    dp[idx] = min(dp[idx], dp[idx-coin]+1)
        return dp[-1] if dp[-1] != float("inf") else -1