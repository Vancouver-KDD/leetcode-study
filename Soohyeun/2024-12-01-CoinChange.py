class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # using dp
        # create an array, length of amount + 1
        # go throught the array and create nested iteration with coins, and check [index-coin] and find minimum

        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                prev = i - coin
                if prev >= 0 and memo[prev] != float('inf'):
                    memo[i] = min(memo[prev]+1, memo[i])

        return memo[amount] if memo[amount] != float('inf') else -1