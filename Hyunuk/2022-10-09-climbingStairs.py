class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i -2]
        return dp[-1]
