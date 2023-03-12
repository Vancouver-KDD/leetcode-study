"""
70. Climbing Stairs
"""

class Solution:

    def climbStairs(self, n: int) -> int:
        # to reach ith step
        # 2 two ways: 1 step from i-1 and 2 step from i-2
        dp = [0] * (n + 1)
        dp[0] = 1 # zero step only 1 way
        dp[1] = 1 # 1 step only 1 way

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
