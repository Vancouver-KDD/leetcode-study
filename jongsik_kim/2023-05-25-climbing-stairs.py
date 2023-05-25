class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, (n + 1)):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]


s = Solution()
print(s.climbStairs(int(input('Enter the number: '))))

# Input: n = 2
# Output: 2

# Input: n = 3
# Output: 3
