class Solution:
    def climbStairs(self, n: int) -> int:
        # basecase
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # ith stair, it can be reached from (i-1)th stair or (i-2)th stair
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]