class Solution:
    def lengthOfLIS(self, nums):
        # Bottom Up DP (Tabulation)
        # Time O(n^2)
        # Space: O(n)

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
