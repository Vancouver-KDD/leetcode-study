class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount + 1)
        memo[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] += memo[i - coin]

        return memo[amount]

# TC: O(m*n) where m=amount and n=len(coins)
# SC: O(m) where m=amount