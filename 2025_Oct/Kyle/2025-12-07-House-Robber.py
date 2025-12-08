class Solution(object):
    def rob(self, nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for money in nums:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
