class Solution:
    def climbStairs(self, n: int) -> int:
        # dp - bottom up (space optimized)
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one
    
        # dp - bottom up (full array)
        # dp = [0] * (n+1)
        # dp[0], dp[1] = 1, 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]