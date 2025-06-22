"""
322. Coin Change / Medium

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        bottom up dynamic programming
        Ex) keep the minimum count for each number
        0 to amount
        dp[0] = 0
        dp[1] = 1
        # if c = 1, [1, 2, 3, 4]
        dp[2] = 1 + dp[1]
        [1, 2, 5]
        dp[2] = min(dp[2], 1 + dp[2 - 2 = 0])
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[num] = min(dp[num], 1 + dp[num - coin])

        return dp[amount] if dp[amount] != (amount + 1) else -1
