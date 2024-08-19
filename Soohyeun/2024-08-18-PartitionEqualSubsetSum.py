class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        dp = [[False] * (subset_sum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for i in range(1, len(nums)+1):
            curr_num = nums[i-1]
            for j in range(subset_sum + 1):
                if j < curr_num:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr_num]

        return dp[-1][-1]
