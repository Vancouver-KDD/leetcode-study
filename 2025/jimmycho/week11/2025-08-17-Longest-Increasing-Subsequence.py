class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = 1
        dp = [[1] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            dp[i][i] = dp[i - 1][i]
            for j in range(i + 1, len(nums) + 1):
                if nums[i - 1] < nums[j - 1]:
                    dp[i][j] = max(dp[i][i] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
                res = max(res, dp[i][j])
        return res
